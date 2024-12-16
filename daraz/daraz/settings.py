# Scrapy settings for daraz project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = "daraz"

SPIDER_MODULES = ["daraz.spiders"]
NEWSPIDER_MODULE = "daraz.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "daraz (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 10  # minimum download delay
AUTOTHROTTLE_ENABLED = True

# Enable retrying requests with a different proxy on failure

SCRAPEOPS_API_KEY = '473cccb8-f8b4-43f9-9494-7ab97c3ebcbd'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    # ...
    'daraz.middlewares.ProxyRotationMiddleware': 200,
    'daraz.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 150,
    # ...
}
PROXIES = ['http://20.44.206.138:80', 'http://218.104.52.188:80', 'http://177.200.239.40:999', 'http://189.173.171.127:999', 'http://94.74.80.88:18081', 'http://47.254.158.115:3127', 'http://49.0.199.132:1337', 'http://147.139.164.26:8080', 'http://49.0.246.130:8103', 'http://49.0.250.196:4145', 'http://39.104.79.145:21025', 'http://123.57.1.16:5555', 'http://47.109.46.223:999', 'http://47.109.53.253:1111', 'http://110.238.111.229:6789', 'http://110.238.116.82:83', 'http://121.40.115.140:8080', 'http://8.208.85.34:1080', 'http://47.100.90.127:45554', 'http://120.79.34.201:8999', 'http://47.113.221.120:55443', 'http://120.79.21.48:8000', 'http://47.92.239.69:8123', 'http://47.92.242.45:82', 'http://47.92.247.250:1081', 'http://39.104.57.170:18081', 'http://47.92.248.197:5000', 'http://139.196.214.238:10001', 'http://49.0.246.130:808', 'http://8.213.129.20:20000', 'http://8.213.129.20:8080', 'http://50.231.0.43:4481', 'http://184.185.105.105:4481', 'http://45.224.149.75:999', 'http://103.152.118.153:8080', 'http://103.76.148.198:8080']

#
# # ROTATING_PROXY_LIST_PATH = 'P:/scraping/proxies.txt'
#


# # Retry many times since proxies often fail
# RETRY_TIMES = 5
# # Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     'scrapy_proxies.RandomProxy': 100,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }
#
# # Proxy list containing entries like
# # http://host1:port
# # http://username:password@host2:port
# # http://host3:port
# # ...
# PROXY_LIST = 'P:/scraping/proxies.txt'
#
#
# # Proxy mode
# # 0 = Every requests have different proxy
# # 1 = Take only one proxy from the list and assign it to every requests
# # 2 = Put a custom proxy to use in the settings
# PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
# CUSTOM_PROXY = "http://host1:port"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "daraz.middlewares.DarazSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "daraz.middlewares.DarazDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "daraz.pipelines.DarazPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
