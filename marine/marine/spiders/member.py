import scrapy

"""
boxes = response.xpath('//ul[@class="uk-list"]/li/div')
name = box.xpath('./h2/a/text()').get()
address = box.xpath('./p/text()[1]').get().strip()
phone = box.xpath('./p/text()[2]').get().split(':')[-1].strip()
category = box.xpath('./p/text()[3]').get().split(':')[-1].strip()
"""


class MemberSpider(scrapy.Spider):
    name = "member"
    allowed_domains = ["mtam.org"]
    start_urls = ["https://mtam.org/members-directory/"]

    def parse(self, response):
        links = response.xpath('//h2[@class="su-post-title"]/a/@href')
        for link in links:
            url = link.get()
            yield response.follow(url=url, callback=self.company_parser)

    def company_parser(self, response):

        name = response.xpath('//h1/text()').get()
        address = response.xpath('//h1/following-sibling::p/text()').get().strip()
        website = response.xpath('//div[@class="uk-card uk-card-body uk-background-muted"]/div/a/@href').get()
        phone = response.xpath('//h3/following-sibling::text()').get().strip()
        category = response.xpath('//h1/following-sibling::div/text()').get()
        if category:
            category = category.split(':')[-1].strip()
        description = response.xpath('//div[@class="uk-card uk-card-body uk-background-muted"]/div/p/text()').get()
        yield {
            'name': name,
            'address': address,
            'website': website,
            'phone': phone,
            'category': category,
            'description': description
        }
