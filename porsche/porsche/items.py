# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PorscheItem(scrapy.Item):
    ## names of fields for the Porsche item
    url = scrapy.Field()
    name = scrapy.Field()
    fuel_economy = scrapy.Field()
    transmission = scrapy.Field()
    exterior = scrapy.Field()
    interior = scrapy.Field()
    body_seating = scrapy.Field()
    drivetrain = scrapy.Field()
    engine = scrapy.Field()
    price = scrapy.Field()
    phone_number = scrapy.Field()
    location = scrapy.Field()
    stock_number = scrapy.Field()
    vin = scrapy.Field()
