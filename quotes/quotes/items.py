# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    thequote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
