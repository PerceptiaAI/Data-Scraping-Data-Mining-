import scrapy
import random


class BatSpider(scrapy.Spider):
    name = "bat"
    start_urls = ["http://httpbin.org/get"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        yield {
            "feeling_lucky": response.text,
            }
