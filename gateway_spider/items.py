# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GatewaySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gateway_name = scrapy.Field()
    protocol_name_between = scrapy.Field()
    protocol_name_upload = scrapy.Field()
    workspace_type = scrapy.Field()
    rechargeable = scrapy.Field()
    input_v = scrapy.Field()
    work_temperature = scrapy.Field()
    description = scrapy.Field()
    other_info = scrapy.Field()
    productor_name = scrapy.Field()
