# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NflScrapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    position = scrapy.Field()
    height_and_weight = scrapy.Field()
    team = scrapy.Field()
