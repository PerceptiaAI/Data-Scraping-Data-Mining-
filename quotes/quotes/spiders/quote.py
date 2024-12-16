import scrapy
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            quotes_item = QuotesItem()
            quotes_item['thequote'] = quote.xpath("./span[@class]/text()").get()
            quotes_item['author'] = quote.xpath("./span/small/text()").get()
            quotes_item["tags"] = quote.xpath("./div/meta/@content").get()
            yield quotes_item

        next_element = response.xpath("//li[@class='next']/a/@href")
        if next_element:
            url = response.urljoin(next_element[0].get())
            yield scrapy.Request(url=url, callback=self.parse)
