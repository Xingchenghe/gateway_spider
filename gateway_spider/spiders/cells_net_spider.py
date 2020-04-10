import scrapy
from scrapy.selector import Selector

# 晓网科技
from gateway_spider.items import GatewaySpiderItem


class CellsNetSpider(scrapy.Spider):
    name = "cells-net"
    start_urls = ['http://www.cells-net.net/gytxsb/gytxsb_338_1.html']
    base_url = "http://www.cells-net.net/gytxsb/"

    def parse(self, response):
        item_infos = response.css('#met-grid li a').extract()
        for item in item_infos:
            item = Selector(text=item)
            href = self.base_url + item.css('a::attr(href)').extract_first()
            # gateway_name = item.css('a::attr(title)').extract_first()
            yield scrapy.Request(url=href, callback=self.parse_gateway)

    def parse_gateway(self, response):
        item_details = response.css('.product-intro ul li::text').extract()
        field_count = 0
        item = GatewaySpiderItem()
        item['gateway_name'] = response.css('h1::text').extract_first()
        item['productor_name'] = '晓网科技'
        item['rechargeable'] = '否'
        item['other_info'] = ''
        item['workspace_type'] = '工业普通级'
        for detail in item_details:
            prop0 = detail.split("：")
            if self.map_key(prop0[0]) == 'other_info':
                item[self.map_key(prop0[0])] = item[self.map_key(prop0[0])] + detail + "、"
            else:
                item[self.map_key(prop0[0])] = prop0[1]
                field_count += 1
        if field_count >= 2:
            self.log(item)

    def map_key(self, key):
        if key == '通讯协议' or key == '串口':
            return 'protocol_name_between'
        if key == '供电电压' or key == '输入电压':
            return 'input_v'
        if key == '工作温度':
            return 'work_temperature'
        else:
            return 'other_info'
