import scrapy
from scrapy.selector import Selector

# 三汇网关
from gateway_spider.items import GatewaySpiderItem


class SynwaySpider(scrapy.Spider):
    name = "synway"
    start_urls = ['http://www.synway.cn/product/1/1/0/0.html', 'http://www.synway.cn/product/1/2/0/1.html',
                  'http://www.synway.cn/product/1/3/0/2.html']
    base_url = "http://www.synway.cn"

    def parse(self, response):
        item_infos = response.css('.pro_main ul li a').extract()
        for item in item_infos:
            item = Selector(text=item)
            href = self.base_url + item.css('a::attr(href)').extract_first()
            yield scrapy.Request(url=href, callback=self.parse_gateway)

    def parse_gateway(self, response):
        item = GatewaySpiderItem()
        item['gateway_name'] = response.css('.tit h3::text').extract_first()
        item['productor_name'] = '杭州三汇网关'
        item['rechargeable'] = '否'
        item['other_info'] = ''
        item['workspace_type'] = '工业普通级'
        item['description'] = response.css('.tit h5::text').extract_first()
        item_details = response.css('.pro_con_box div:nth-child(2) ol p::text').extract()
        for detail in item_details:
            self.log(detail.strip())
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
