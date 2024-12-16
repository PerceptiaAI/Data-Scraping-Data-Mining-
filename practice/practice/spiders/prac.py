import scrapy
from scrapy.http import FormRequest


class PracSpider(scrapy.Spider):
    name = "prac"
    allowed_domains = ["quotes.toscrape.com"]





    def start_requests(self):
        login_url = 'http://quotes.toscrape.com/login'
        return scrapy.Request(login_url, callback=self.login)

    def login(self, response):
        token = response.css("form input[name=csrf_token]::attr(value)").extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': 'foobar',
                                                   'username': 'foobar'},
                                         callback=self.start_scraping)

    def start_scraping(self, response):
        ## Insert code to start scraping pages once logged in
        pass
