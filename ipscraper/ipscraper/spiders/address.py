import scrapy



class AddressSpider(scrapy.Spider):
    name = "address"
    start_urls = ["http://icanhazip.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            # check proxy
            'add': response.meta['proxy'],
        }
