#!/usr/bin/env python3
"""
Jekyll Site Validation Script
Validates that all required files exist and are properly configured.
"""

import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path

def validate_jekyll_setup():
    """Validate Jekyll site setup and configuration."""
    print("🔍 Validating Jekyll RSS Feed Hub Setup...\n")
    
    errors = []
    warnings = []
    
    # Check required files
    required_files = [
        '_config.yml',
        'Gemfile', 
        'index.html',
        'about.md',
        'feeds.html',
        '404.html',
        'robots.txt',
        'sitemap.xml',
        '_layouts/default.html',
        '.github/workflows/scrape-and-generate-rss.yml',
        'scripts/enhanced_scraper.py',
        'scripts/monitor.py',
        'scripts/config.py',
        'scripts/feed_generator.py'
    ]
    
    print("📁 Checking required files:")
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path}")
            errors.append(f"Missing required file: {file_path}")
    
    # Check RSS feeds
    print("\n📡 Checking RSS feeds:")
    # Only validate active feeds; EEI (LinkedIn) feed disabled.
    rss_files = ['ai_rss_feed.xml']
    for rss_file in rss_files:
        if os.path.exists(rss_file):
            try:
                ET.parse(rss_file)
                print(f"  ✅ {rss_file} (valid XML)")
            except ET.ParseError as e:
                print(f"  ⚠️  {rss_file} (invalid XML: {e})")
                warnings.append(f"RSS feed {rss_file} has XML parsing errors")
        else:
            print(f"  ❌ {rss_file}")
            errors.append(f"Missing RSS feed: {rss_file}")
    
    # Check status file
    print("\n📊 Checking status monitoring:")
    status_path = 'api/rss_status.json'
    if os.path.exists(status_path):
        try:
            with open(status_path, 'r') as f:
                status_data = json.load(f)
            print(f"  ✅ {status_path} (valid JSON)")
            
            # Check feed status
            if 'feeds' in status_data:
                for feed_name, feed_data in status_data['feeds'].items():
                    entry_count = feed_data.get('entry_count', 0)
                    if entry_count > 0:
                        print(f"  ✅ {feed_name}: {entry_count} entries")
                    else:
                        print(f"  ⚠️  {feed_name}: {entry_count} entries")
                        warnings.append(f"Feed {feed_name} has no entries")
            
        except json.JSONDecodeError as e:
            print(f"  ❌ {status_path} (invalid JSON: {e})")
            errors.append(f"{status_path} is not valid JSON")
    else:
        print(f"  ❌ {status_path}")
        errors.append(f"Missing {status_path}")
    
    # Check GitHub Actions workflow
    print("\n🚀 Checking GitHub Actions workflow:")
    workflow_path = '.github/workflows/scrape-and-generate-rss.yml'
    if os.path.exists(workflow_path):
        with open(workflow_path, 'r') as f:
            workflow_content = f.read()
        
        required_jobs = ['scrape-and-generate-rss', 'deploy-on-push', 'deploy-after-scrape']
        for job in required_jobs:
            if job in workflow_content:
                print(f"  ✅ Job: {job}")
            else:
                print(f"  ❌ Job: {job}")
                errors.append(f"Missing GitHub Actions job: {job}")
        
        if 'actions/deploy-pages@v4' in workflow_content:
            print(f"  ✅ GitHub Pages deployment configured")
        else:
            print(f"  ⚠️  GitHub Pages deployment not found")
            warnings.append("GitHub Pages deployment may not be configured")
    
    # Summary
    print("\n" + "="*50)
    print("📋 VALIDATION SUMMARY")
    print("="*50)
    
    if not errors and not warnings:
        print("🎉 ALL CHECKS PASSED! Your Jekyll RSS Feed Hub is ready for deployment.")
        print("\n🚀 Next steps:")
        print("1. Push changes to GitHub")
        print("2. Enable GitHub Pages in repository settings")
        print("3. Set source to 'GitHub Actions'")
        print("4. Your site will be live!")
        return True
    
    if errors:
        print(f"❌ {len(errors)} ERROR(S) FOUND:")
        for error in errors:
            print(f"   • {error}")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNING(S) FOUND:")
        for warning in warnings:
            print(f"   • {warning}")
    
    if errors:
        print("\n🔧 Please fix the errors above before deploying.")
        return False
    else:
        print("\n✅ No critical errors found. Warnings should be addressed but won't prevent deployment.")
        return True

if __name__ == "__main__":
    success = validate_jekyll_setup()
    exit(0 if success else 1)
