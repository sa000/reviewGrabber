# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Review(scrapy.Item):
	#Intiliaze fields for the review
    helpful=scrapy.Field()
    clarity=scrapy.Field()
    easy=scrapy.Field()
    course=scrapy.Field()
    comment=scrapy.Field
    date=scrapy.Field
