from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Event, Lock
import unittest
from unittest.mock import patch

from pipeline.llm_client import OpenAIAPIClient, OpenAIWorkloadIdentityTokenProvider


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class FakeOpenAISession:
    def __init__(self):
        self.headers = {}
        self.posts = []

    def post(self, url, json=None, headers=None, timeout=None):
        self.posts.append({"url": url, "json": json, "timeout": timeout, "headers": headers or dict(self.headers)})
        return FakeResponse(
            {
                "data": [{"embedding": [0.1, 0.2, 0.3]}],
                "usage": {"total_tokens": 3},
            }
        )


class FakeWIFSession:
    def __init__(self):
        self.gets = []
        self.posts = []

    def get(self, url, headers=None, timeout=None):
        self.gets.append({"url": url, "headers": headers or {}, "timeout": timeout})
        return FakeResponse({"value": "github-oidc-jwt"})

    def post(self, url, json=None, headers=None, timeout=None):
        self.posts.append({"url": url, "json": json or {}, "headers": headers or {}, "timeout": timeout})
        return FakeResponse({"access_token": "openai-access-token", "expires_in": 3600})


class BlockingWIFSession(FakeWIFSession):
    def __init__(self):
        super().__init__()
        self.first_get_started = Event()
        self.release_first_get = Event()
        self.concurrent_get_started = Event()
        self.lock = Lock()

    def get(self, url, headers=None, timeout=None):
        with self.lock:
            call_number = len(self.gets) + 1
            self.gets.append({"url": url, "headers": headers or {}, "timeout": timeout})
        if call_number == 1:
            self.first_get_started.set()
            self.release_first_get.wait(timeout=1.0)
        else:
            self.concurrent_get_started.set()
        return FakeResponse({"value": "github-oidc-jwt"})


class ConcurrentOpenAISession(FakeOpenAISession):
    def __init__(self, barrier, used_sessions, lock):
        super().__init__()
        self.barrier = barrier
        self.used_sessions = used_sessions
        self.lock = lock

    def post(self, url, json=None, headers=None, timeout=None):
        with self.lock:
            self.used_sessions.add(id(self))
        self.barrier.wait()
        self.posts.append({"url": url, "json": json, "headers": headers or dict(self.headers), "timeout": timeout})
        return FakeResponse(
            {
                "data": [{"embedding": [0.1, 0.2, 0.3]}],
                "usage": {"total_tokens": 3},
            }
        )


class OpenAIClientTests(unittest.TestCase):
    def test_openai_client_strips_github_models_vendor_prefix_on_wire(self):
        client = OpenAIAPIClient(api_key="test-openai-key", timeout_sec=7)
        fake_session = FakeOpenAISession()
        client.session = fake_session

        result = client.embed(["hello"], model="openai/text-embedding-3-small")

        self.assertEqual(result["model"], "openai/text-embedding-3-small")
        self.assertEqual(fake_session.posts[0]["url"], "https://api.openai.com/v1/embeddings")
        self.assertEqual(fake_session.posts[0]["json"]["model"], "text-embedding-3-small")
        self.assertEqual(fake_session.posts[0]["headers"]["Authorization"], "Bearer test-openai-key")
        self.assertEqual(fake_session.posts[0]["timeout"], 7)

    def test_workload_identity_provider_exchanges_github_oidc_token_and_caches_access_token(self):
        fake_session = FakeWIFSession()
        provider = OpenAIWorkloadIdentityTokenProvider(
            identity_provider_id="idp_123",
            service_account_id="svc_123",
            audience="openai-audience",
            request_url="https://token.actions.githubusercontent.com?api-version=2",
            request_token="github-request-token",
            session=fake_session,
            clock=lambda: 1000.0,
        )

        token = provider.get_token()
        cached_token = provider.get_token()

        self.assertEqual(token, "openai-access-token")
        self.assertEqual(cached_token, "openai-access-token")
        self.assertEqual(len(fake_session.gets), 1)
        self.assertEqual(len(fake_session.posts), 1)
        self.assertIn("api-version=2", fake_session.gets[0]["url"])
        self.assertIn("audience=openai-audience", fake_session.gets[0]["url"])
        self.assertEqual(fake_session.gets[0]["headers"]["Authorization"], "bearer github-request-token")
        self.assertEqual(fake_session.posts[0]["url"], "https://auth.openai.com/oauth/token")
        self.assertEqual(fake_session.posts[0]["json"]["subject_token"], "github-oidc-jwt")
        self.assertEqual(fake_session.posts[0]["json"]["subject_token_type"], "urn:ietf:params:oauth:token-type:jwt")
        self.assertEqual(fake_session.posts[0]["json"]["identity_provider_id"], "idp_123")
        self.assertEqual(fake_session.posts[0]["json"]["service_account_id"], "svc_123")

    def test_concurrent_workload_identity_requests_share_one_token_refresh(self):
        fake_session = BlockingWIFSession()
        provider = OpenAIWorkloadIdentityTokenProvider(
            identity_provider_id="idp_123",
            service_account_id="svc_123",
            audience="openai-audience",
            request_url="https://token.actions.githubusercontent.com",
            request_token="github-request-token",
            session=fake_session,
            clock=lambda: 1000.0,
        )

        with ThreadPoolExecutor(max_workers=4) as executor:
            first = executor.submit(provider.get_token)
            self.assertTrue(fake_session.first_get_started.wait(timeout=1.0))
            others = [executor.submit(provider.get_token) for _index in range(3)]
            concurrent_refresh = fake_session.concurrent_get_started.wait(timeout=0.2)
            fake_session.release_first_get.set()
            tokens = [first.result(), *(future.result() for future in others)]

        self.assertFalse(concurrent_refresh)
        self.assertEqual(tokens, ["openai-access-token"] * 4)
        self.assertEqual(len(fake_session.gets), 1)
        self.assertEqual(len(fake_session.posts), 1)

    def test_concurrent_openai_calls_use_thread_local_sessions(self):
        barrier = Barrier(2, timeout=1.0)
        used_sessions = set()
        lock = Lock()

        with patch(
            "pipeline.llm_client.requests.Session",
            side_effect=lambda: ConcurrentOpenAISession(barrier, used_sessions, lock),
        ):
            client = OpenAIAPIClient(api_key="test-openai-key")
            with ThreadPoolExecutor(max_workers=2) as executor:
                results = list(executor.map(lambda text: client.embed([text]), ["one", "two"]))

        self.assertEqual(len(results), 2)
        self.assertEqual(len(used_sessions), 2)


if __name__ == "__main__":
    unittest.main()
