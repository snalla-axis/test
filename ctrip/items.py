# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class CtripItem(scrapy.Item):
	hotel_id=scrapy.Field()
	loc_id=scrapy.Field()
	city=scrapy.Field()
	hotel_name=scrapy.Field()
