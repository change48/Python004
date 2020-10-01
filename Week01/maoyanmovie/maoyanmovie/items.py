# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MaoyanmovieItem(scrapy.Item):
    mname = scrapy.Field()
    mtype = scrapy.Field()
    mtime = scrapy.Field()


