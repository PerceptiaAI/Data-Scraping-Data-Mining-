import scrapy

import random

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]



class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': random.choice(user_agent_list)},meta={
                'proxy': "http://144.49.99.190:8080"
            })

    def parse(self, response):
        movies = response.xpath("//ul[contains(@class, 'ipc-metadata-list')]/li")
        for movie in movies:
            yield {
                "title": movie.xpath(".//h3/text()").get(),
                "year": movie.xpath("./div[2]/div/div/div[2]/span[1]/text()").get(),
                "rating": movie.xpath("./div[2]/div/div/div[2]/span[2]/text()").get()
            }
