# -*- coding: utf-8 -*-

# Scrapy settings for myFirstChong project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myFirstChong'

SPIDER_MODULES = ['myFirstChong.spiders']
NEWSPIDER_MODULE = 'myFirstChong.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myFirstChong (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myFirstChong.middlewares.MyfirstchongSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myFirstChong.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html




# FEED_EXPORTERS_BASE = {
    # 'json' : 'myFirstChong.xxx.chongxie' , 
    # 'jsonlines' : 'scrapy.contrib.exporter.JsonLinesItemExporter',

# }


# ITEM_PIPELINES = {
# #    'myFirstChong.pipelines.MyfirstchongPipeline': 300,
# #    'scrapy.pipelines.images.ImagesPipeline': 100 ,
#    'myFirstChong.xxx.chongxie' : 100 #-------------------------------------------------
# #    'scrapy.exrensions.pipelines.images.ImagesPipeline':100
# }
#-----------------------------------------------------------------------------------------------
# import os
# projectpath = os.path.abspath(os.path.dirname(__file__))
# aaa = os.path.join(projectpath , "myImages1")
# IMAGES_STORE = aaa

# #feedExport
# #文件导出的配置

# # FEED_FORMAT = "json"   

# FEED_STORAGES_BASE = {
#     '': 'scrapy.extensions.feedexport.FileFeedStorage',
#     'file': 'scrapy.extensions.feedexport.FileFeedStorage',
#     'stdout': 'scrapy.extensions.feedexport.StdoutFeedStorage',
#     's3': 'scrapy.extensions.feedexport.S3FeedStorage',
#     'ftp': 'scrapy.extensions.feedexport.FTPFeedStorage',
# }

# FEED_URI = "ftp://dangsh:5801200@012.3vftp.com/ddd.json"



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
