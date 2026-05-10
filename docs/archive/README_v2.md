<!-- markdownlint-disable -->

# GitHub Action: Table Scraper to RSS Feed - Enhanced

A sophisticated GitHub Action that scrapes table data from websites to generate an AI news RSS feed automatically.

## 🚀 New Features (v2.1)

- **🔄 Automated RSS Feed**: GAI Insights table scraping (60‑day retention + archive)
- **📊 Health Monitoring**: Automated RSS feed health checks and status reports
- **⚙️ Configuration Management**: Centralized configuration for easy customization
- **🛡️ Enhanced Error Handling**: Robust error handling with retry mechanisms
- **📈 Better Change Detection**: Intelligent change detection to avoid unnecessary updates
- **📝 Structured Logging**: Comprehensive logging for debugging and monitoring
- **🎯 Smart Content Filtering**: AI-focused content filtering and normalization
- **🌐 Multi-Source Aggregation**: Merge external RSS feeds into a single local feed with retention & archive
- **🗂️ Dual Archives**: Separate archive for both GAI feed and aggregated external feed

## 📁 Project Structure

```
├── scripts/scrape_to_rss.py  # Original scraper (legacy)
├── scripts/enhanced_scraper.py # New enhanced scraper with better architecture
├── scripts/monitor.py        # RSS feed health monitoring
├── scripts/config.py         # Centralized configuration
├── requirements.txt          # Python dependencies
├── .github/workflows/        # GitHub Actions workflows
│   └── scrape-and-generate-rss.yml
├── ai_rss_feed.xml          # GAI Insights RSS feed
└── api/rss_status.json      # Health monitoring report
```

## 📊 RSS Feeds Generated

### 1. GAI Insights RSS Feed (`ai_rss_feed.xml`)
- Scrapes the ratings table from [gaiinsights.com/ratings](https://gaiinsights.com/ratings)
- Updates every 8 hours
- Includes rating tags: Essential [!], Important [*], Optional [~]

Archive: `ai_rss_feed_archive.xml` retains items older than 60 days.

### 2. Aggregated External Feeds (Multi-Feed Capable)
- Define one OR many aggregated feeds in `_config.yml` under `aggregated_feeds`
- Supports legacy single-mapping OR list-of-mappings schemas
- Each feed: retention, attribution, archive, max items, independent sources
- Archive file auto-generated: `<output>_archive.xml`

Single feed (legacy style):

```yaml
aggregated_feeds:
   enabled: true
   output: "/aggregated_external.xml"
   title: "Aggregated External AI & Tech News"
   link: "https://rss.tedt.org/aggregated_external.xml"
   description: "Merged headlines from configured external sources"
   max_items: 150
   retention_days: 60
   source_attribution: title   # title|description|none
   sources:
      - "https://feeds.arstechnica.com/arstechnica/technology-lab"
      - "https://www.infoworld.com/index.rss"
      - "https://www.techrepublic.com/rssfeeds/articles/"
      - "https://www.zdnet.com/news/rss.xml"
```

   Multiple feeds (new style):

   ```yaml
   aggregated_feeds:
      - key: external_ai
         enabled: true
         output: "/aggregated_external.xml"
         title: "Aggregated External AI & Tech News"
         max_items: 150
         retention_days: 60
         source_attribution: title
         sources:
            - "https://feeds.arstechnica.com/arstechnica/technology-lab"
            - "https://www.zdnet.com/news/rss.xml"
      - key: security
         enabled: true
         output: "/aggregated_security.xml"
         title: "Security & Privacy Tech News"
         max_items: 120
         retention_days: 45
         source_attribution: description
         sources:
            - "https://krebsonsecurity.com/feed/"
            - "https://feeds.feedburner.com/TheHackersNews"
   ```

   Resulting local files: `aggregated_external.xml`, `aggregated_external_archive.xml`, `aggregated_security.xml`, `aggregated_security_archive.xml`

## 🔧 Configuration

All settings are centralized in `scripts/config.py`:

```python
# URL target
GAI_INSIGHTS_URL = "https://gaiinsights.com/ratings"

# Scraping settings
SCRAPING_CONFIG = {
    "page_load_timeout": 30,
    "dynamic_content_wait": 10,
    "max_articles_per_feed": 50
}

# Content filtering
CONTENT_FILTERS = {
    "ai_keywords": ["ai", "artificial intelligence", "machine learning"],
    "min_title_length": 15
}
```

## 📈 Health Monitoring

The project includes comprehensive health monitoring:

- **Automatic Checks**: Validates RSS feed structure and content
- **Status Reports**: Generates JSON status reports with detailed metrics
- **GitHub Actions Summary**: Creates visual status summaries in GitHub Actions
- **Error Tracking**: Tracks and reports errors with detailed diagnostics

## 🎯 Advanced Features

### Smart Content Detection
- Intelligent column identification for flexible table structures
- Duplicate detection and removal

### Robust Error Handling
- Retry mechanisms for failed requests
- Graceful degradation when services are unavailable
- Comprehensive error logging and reporting

### Performance Optimization
- Efficient change detection to avoid unnecessary processing
- Configurable timeouts and retry policies
- Resource cleanup and memory management

## 🚀 Getting Started

### Local Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Enhanced Scraper**:
   ```bash
   python -m scripts.enhanced_scraper
   ```

3. **Run Health Monitoring**:
   ```bash
   python -m scripts.monitor
   ```

### GitHub Actions Setup

The workflow runs automatically every 8 hours and can be triggered manually:

1. **Automatic**: Every 8 hours at minute 0
2. **Manual**: Via GitHub Actions UI (`workflow_dispatch`)

## 📊 Monitoring and Alerts

### RSS Feed Status Report

The monitoring system generates detailed reports including:

- Feed existence and validity
- Entry counts and content quality
- File sizes and last update times
- Error tracking and diagnostics

### GitHub Actions Integration

- Visual status summaries in GitHub Actions
- Automated commit and push of updated feeds
- Error notifications and status badges

## 🔄 Workflow Process

1. **Scraping Phase**:
   - Scrape GAI Insights table data
   - Extract table rows and transform into RSS entries

2. **Processing Phase**:
   - Generate RSS feeds with proper formatting
   - Apply content filtering and validation
   - Detect changes from previous runs

3. **Monitoring Phase**:
   - Validate RSS feed health
   - Generate status reports
   - Create GitHub Actions summaries

4. **Publishing Phase**:
   - Commit updated feeds to repository
   - Update status reports
   - Trigger any configured notifications

## 🛠️ Customization

### Adding New Data Sources

1. Create a new scraper class in `scripts/enhanced_scraper.py`
2. Add configuration in `scripts/config.py`
3. Update the RSS generation logic
4. Add monitoring for the new feed

### Modifying Content Filters

Edit the `CONTENT_FILTERS` in `scripts/config.py`:

```python
CONTENT_FILTERS = {
    "ai_keywords": ["your", "custom", "keywords"],
    "excluded_domains": ["spam.com"],
    "min_title_length": 10
}
```

### Adjusting Scraping Behavior

Modify `SCRAPING_CONFIG` in `scripts/config.py`:

```python
SCRAPING_CONFIG = {
    "page_load_timeout": 45,
    "retry_attempts": 5,
    "max_articles_per_feed": 100
}
```

## 📱 Accessing RSS Feeds

Your RSS feeds will be available at:

- **GAI Insights**: `https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/ai_rss_feed.xml`

## 🐛 Troubleshooting

### Common Issues

1. **Empty RSS Feed**: No content found
   - Check status report in `api/rss_status.json`
   - Verify source website structure hasn't changed
   - Review error logs in GitHub Actions

2. **Timeout Errors**: Slow page loading
   - Increase timeout values in `scripts/config.py`
   - Check GitHub Actions runner performance
   - Consider reducing content processing

### Debug Information

Enable debug mode by setting environment variable:
```bash
export DEBUG=true
python -m scripts.enhanced_scraper
```

This generates debug HTML files for inspection.

## 📈 Performance Metrics

The system tracks various performance metrics:

- Scraping success rates
- Feed generation times
- Content quality scores
- Error frequencies

## 🔮 Future Enhancements

- [x] Multi-source RSS aggregation
- [ ] Advanced content analysis and tagging
- [ ] Real-time notifications for high-priority content
- [ ] Machine learning-based content recommendation
- [ ] API endpoints for programmatic access
- [ ] Advanced analytics and reporting
- [ ] Integration with additional social platforms

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
