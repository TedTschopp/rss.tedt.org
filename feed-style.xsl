<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rss1="http://purl.org/rss/1.0/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    exclude-result-prefixes="atom content rdf rss1 dc">
    
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <title><xsl:value-of select="/rss/channel/title | /atom:feed/atom:title | /rdf:RDF/rss1:channel/rss1:title | /rdf:RDF/channel/title"/></title>
                
                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"/>
                
                <!-- Font Awesome -->
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"/>
                
                <!-- Google Fonts -->
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
                
                <style>
                    :root {
                        --bs-primary: #00446f;
                        --bs-secondary: #e86027;
                        --bs-success: #00b339;
                        --bs-info: #00a9e0;
                        --bs-warning: #f2bc57;
                        --bs-danger: #f90041;
                        --bs-body-bg: #f8f6f0;
                        --bs-body-color: #1f2126;
                        --bs-link-color: #007bff;
                    }
                    
                    body {
                        font-family: 'Inter', sans-serif;
                        line-height: 1.6;
                        color: var(--bs-body-color);
                        background: var(--bs-body-bg);
                    }
                    
                    .feed-header {
                        background: linear-gradient(135deg, var(--bs-primary) 0%, var(--bs-info) 100%);
                        color: white;
                        padding: 2rem 0;
                        margin-bottom: 2rem;
                    }
                    
                    .feed-header h1 {
                        font-weight: 700;
                        margin-bottom: 0.5rem;
                    }
                    
                    .feed-header p {
                        opacity: 0.9;
                        margin-bottom: 0;
                    }
                    
                    .subscribe-notice {
                        background: #fcf2dd;
                        border: 1px solid var(--bs-warning);
                        border-radius: 0.5rem;
                        padding: 1rem 1.5rem;
                        margin-bottom: 2rem;
                    }
                    
                    .subscribe-notice i {
                        color: #614b23;
                    }
                    
                    .feed-item {
                        background: white;
                        border-radius: 0.5rem;
                        padding: 1.5rem;
                        margin-bottom: 1rem;
                        box-shadow: 0 0.125rem 0.25rem rgba(7, 9, 15, 0.075);
                        transition: box-shadow 0.15s ease-in-out;
                    }
                    
                    .feed-item:hover {
                        box-shadow: 0 0.5rem 1rem rgba(7, 9, 15, 0.15);
                    }
                    
                    .feed-item h3 {
                        font-size: 1.1rem;
                        font-weight: 600;
                        margin-bottom: 0.5rem;
                    }
                    
                    .feed-item h3 a {
                        color: var(--bs-primary);
                        text-decoration: none;
                    }
                    
                    .feed-item h3 a:hover {
                        color: var(--bs-info);
                    }
                    
                    .feed-item .meta {
                        font-size: 0.85rem;
                        color: #676869;
                        margin-bottom: 0.75rem;
                    }
                    
                    .feed-item .description {
                        color: #4f5052;
                        font-size: 0.95rem;
                    }
                    
                    /* Priority styling */
                    .priority-essential {
                        border-left: 4px solid var(--bs-danger);
                    }
                    
                    .priority-important {
                        border-left: 4px solid var(--bs-warning);
                    }
                    
                    .priority-optional {
                        border-left: 4px solid #676869;
                    }
                    
                    .pri-badge {
                        font-size: 0.65rem;
                        letter-spacing: 0.5px;
                        text-transform: uppercase;
                        padding: 2px 6px;
                        border-radius: 3px;
                        font-weight: 600;
                        color: #fff;
                        margin-right: 8px;
                    }
                    
                    .pri-badge.essential {
                        background: var(--bs-danger);
                    }
                    
                    .pri-badge.important {
                        background: var(--bs-warning);
                        color: #222;
                    }
                    
                    .pri-badge.optional {
                        background: #676869;
                    }
                    
                    .footer {
                        background: var(--bs-primary);
                        color: white;
                        padding: 2rem 0;
                        margin-top: 3rem;
                    }
                    
                    .footer a {
                        color: rgba(255,255,255,0.7);
                    }
                    
                    .footer a:hover {
                        color: white;
                    }
                </style>
            </head>
            <body>
                <!-- Header -->
                <header class="feed-header">
                    <div class="container">
                        <h1>
                            <i class="fas fa-rss me-2"></i>
                            <xsl:value-of select="/rss/channel/title | /atom:feed/atom:title | /rdf:RDF/rss1:channel/rss1:title | /rdf:RDF/channel/title"/>
                        </h1>
                        <p><xsl:value-of select="/rss/channel/description | /atom:feed/atom:subtitle | /rdf:RDF/rss1:channel/rss1:description | /rdf:RDF/channel/description"/></p>
                    </div>
                </header>
                
                <main class="container">
                    <!-- Subscribe Notice -->
                    <div class="subscribe-notice">
                        <i class="fas fa-info-circle me-2"></i>
                        <strong>This is an RSS feed.</strong> 
                        Subscribe by copying the URL from your browser's address bar into your favorite feed reader.
                        <a href="https://rss.tedt.org/" class="ms-2">← Back to RSS Feed Hub</a>
                    </div>
                    
                    <!-- Feed Info -->
                    <div class="row mb-4">
                        <div class="col-md-6">
                            <strong>Feed URL:</strong>
                            <code class="ms-2"><xsl:value-of select="/rss/channel/link | /atom:feed/atom:link[@rel='self']/@href | /rdf:RDF/rss1:channel/rss1:link | /rdf:RDF/channel/link"/></code>
                        </div>
                        <div class="col-md-6 text-md-end">
                            <strong>Last Updated:</strong>
                            <span class="ms-2"><xsl:value-of select="/rss/channel/lastBuildDate | /atom:feed/atom:updated | /rdf:RDF/rss1:channel/dc:date | /rdf:RDF/channel/dc:date"/></span>
                        </div>
                    </div>
                    
                    <!-- RSS 2.0 Items -->
                    <xsl:for-each select="/rss/channel/item">
                        <xsl:variable name="title" select="title"/>
                        <xsl:variable name="priorityClass">
                            <xsl:choose>
                                <xsl:when test="contains($title, '[ ! ]')">priority-essential</xsl:when>
                                <xsl:when test="contains($title, '[ * ]')">priority-important</xsl:when>
                                <xsl:when test="contains($title, '[ ~ ]')">priority-optional</xsl:when>
                                <xsl:otherwise></xsl:otherwise>
                            </xsl:choose>
                        </xsl:variable>
                        <article class="feed-item {$priorityClass}">
                            <h3>
                                <xsl:choose>
                                    <xsl:when test="contains($title, '[ ! ]')">
                                        <span class="pri-badge essential">Essential</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ * ]')">
                                        <span class="pri-badge important">Important</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ ~ ]')">
                                        <span class="pri-badge optional">Optional</span>
                                    </xsl:when>
                                </xsl:choose>
                                <a href="{link}" target="_blank" rel="noopener">
                                    <xsl:choose>
                                        <xsl:when test="contains($title, '[ ! ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ! ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ * ]')">
                                            <xsl:value-of select="substring-before($title, ' [ * ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ ~ ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ~ ]')"/>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <xsl:value-of select="$title"/>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </a>
                            </h3>
                            <div class="meta">
                                <i class="far fa-calendar-alt me-1"></i>
                                <xsl:value-of select="pubDate"/>
                            </div>
                            <div class="description">
                                <xsl:value-of select="description"/>
                            </div>
                        </article>
                    </xsl:for-each>
                    
                    <!-- Atom Items -->
                    <xsl:for-each select="/atom:feed/atom:entry">
                        <xsl:variable name="title" select="atom:title"/>
                        <xsl:variable name="priorityClass">
                            <xsl:choose>
                                <xsl:when test="contains($title, '[ ! ]')">priority-essential</xsl:when>
                                <xsl:when test="contains($title, '[ * ]')">priority-important</xsl:when>
                                <xsl:when test="contains($title, '[ ~ ]')">priority-optional</xsl:when>
                                <xsl:otherwise></xsl:otherwise>
                            </xsl:choose>
                        </xsl:variable>
                        <article class="feed-item {$priorityClass}">
                            <h3>
                                <xsl:choose>
                                    <xsl:when test="contains($title, '[ ! ]')">
                                        <span class="pri-badge essential">Essential</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ * ]')">
                                        <span class="pri-badge important">Important</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ ~ ]')">
                                        <span class="pri-badge optional">Optional</span>
                                    </xsl:when>
                                </xsl:choose>
                                <a href="{atom:link/@href}" target="_blank" rel="noopener">
                                    <xsl:choose>
                                        <xsl:when test="contains($title, '[ ! ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ! ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ * ]')">
                                            <xsl:value-of select="substring-before($title, ' [ * ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ ~ ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ~ ]')"/>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <xsl:value-of select="$title"/>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </a>
                            </h3>
                            <div class="meta">
                                <i class="far fa-calendar-alt me-1"></i>
                                <xsl:value-of select="atom:published | atom:updated"/>
                            </div>
                            <div class="description">
                                <xsl:value-of select="atom:summary | atom:content"/>
                            </div>
                        </article>
                    </xsl:for-each>
                    
                    <!-- RSS 1.0 (RDF) Items - with namespace -->
                    <xsl:for-each select="/rdf:RDF/rss1:item">
                        <xsl:variable name="title" select="rss1:title"/>
                        <xsl:variable name="priorityClass">
                            <xsl:choose>
                                <xsl:when test="contains($title, '[ ! ]')">priority-essential</xsl:when>
                                <xsl:when test="contains($title, '[ * ]')">priority-important</xsl:when>
                                <xsl:when test="contains($title, '[ ~ ]')">priority-optional</xsl:when>
                                <xsl:otherwise></xsl:otherwise>
                            </xsl:choose>
                        </xsl:variable>
                        <article class="feed-item {$priorityClass}">
                            <h3>
                                <xsl:choose>
                                    <xsl:when test="contains($title, '[ ! ]')">
                                        <span class="pri-badge essential">Essential</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ * ]')">
                                        <span class="pri-badge important">Important</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ ~ ]')">
                                        <span class="pri-badge optional">Optional</span>
                                    </xsl:when>
                                </xsl:choose>
                                <a href="{rss1:link}" target="_blank" rel="noopener">
                                    <xsl:choose>
                                        <xsl:when test="contains($title, '[ ! ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ! ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ * ]')">
                                            <xsl:value-of select="substring-before($title, ' [ * ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ ~ ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ~ ]')"/>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <xsl:value-of select="$title"/>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </a>
                            </h3>
                            <div class="meta">
                                <i class="far fa-calendar-alt me-1"></i>
                                <xsl:value-of select="dc:date"/>
                            </div>
                            <div class="description">
                                <xsl:value-of select="rss1:description"/>
                            </div>
                        </article>
                    </xsl:for-each>
                    
                    <!-- RSS 1.0 (RDF) Items - without namespace prefix -->
                    <xsl:for-each select="/rdf:RDF/item">
                        <xsl:variable name="title" select="title"/>
                        <xsl:variable name="priorityClass">
                            <xsl:choose>
                                <xsl:when test="contains($title, '[ ! ]')">priority-essential</xsl:when>
                                <xsl:when test="contains($title, '[ * ]')">priority-important</xsl:when>
                                <xsl:when test="contains($title, '[ ~ ]')">priority-optional</xsl:when>
                                <xsl:otherwise></xsl:otherwise>
                            </xsl:choose>
                        </xsl:variable>
                        <article class="feed-item {$priorityClass}">
                            <h3>
                                <xsl:choose>
                                    <xsl:when test="contains($title, '[ ! ]')">
                                        <span class="pri-badge essential">Essential</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ * ]')">
                                        <span class="pri-badge important">Important</span>
                                    </xsl:when>
                                    <xsl:when test="contains($title, '[ ~ ]')">
                                        <span class="pri-badge optional">Optional</span>
                                    </xsl:when>
                                </xsl:choose>
                                <a href="{link}" target="_blank" rel="noopener">
                                    <xsl:choose>
                                        <xsl:when test="contains($title, '[ ! ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ! ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ * ]')">
                                            <xsl:value-of select="substring-before($title, ' [ * ]')"/>
                                        </xsl:when>
                                        <xsl:when test="contains($title, '[ ~ ]')">
                                            <xsl:value-of select="substring-before($title, ' [ ~ ]')"/>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <xsl:value-of select="$title"/>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </a>
                            </h3>
                            <div class="meta">
                                <i class="far fa-calendar-alt me-1"></i>
                                <xsl:value-of select="dc:date"/>
                            </div>
                            <div class="description">
                                <xsl:value-of select="description"/>
                            </div>
                        </article>
                    </xsl:for-each>
                </main>
                
                <!-- Footer -->
                <footer class="footer">
                    <div class="container text-center">
                        <p>
                            <a href="https://rss.tedt.org/">RSS Feed Hub</a>
                            <span class="mx-2">•</span>
                            Powered by Jekyll
                        </p>
                    </div>
                </footer>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
