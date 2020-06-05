# -*- coding: utf-8 -*-
from scrapy.spiders import Request,CrawlSpider
from urllib.parse import urljoin
from CPIC_scrapy.items import CpicScrapyItem as itm
import os


class CPICspider(CrawlSpider):
    name='cpic_scrapy'
    allowed_domains=['cpic.com.cn']
    start_urls=["http://www.cpic.com.cn/baike/qichebaoxian/"]

    # "http://www.cpic.com.cn/baike/yanglaobaoxian/","http://www.cpic.com.cn/baike/yiliaobaoxian/",\
    #             "http://www.cpic.com.cn/baike/shiyebaoxian/","http://www.cpic.com.cn/baike/gongshangbaoxian/","http://www.cpic.com.cn/baike/shengyubaoxian/",\
    #             "http://www.cpic.com.cn/baike/licaibaoxian/","http://www.cpic.com.cn/baike/lvyoubaoxian/"]
 

    def parse(self,response):
        for su in self.start_urls:
            max_page=4 #偷懒。。。
            #next_url=response.css('.a1::attr(href)').extract()[-1]
            #response.xpath("//div[@class="bxmian"]/div[@class="bx_l"]/div[@class="feilei"]/ul[@class="listnews"]/div[@class="text-c"]/a[@class="a1"]/@href").extract()
            for m in range(1,(max_page+1)):
                if m == 1:
                    n_url=su
                else:
                    n_url=su+"list_%s.html"%m
                yield Request(n_url,callback=self.get_texturl)


    def get_texturl(self,response):
        base_url="http://www.cpic.com.cn"
        #xpath("//div[@class="bxmian"]/div[@class="bx_l"]/div[@class="feilei"]/ul/ul[@class="listnews"]/li/a/@href").extract())
        t_url=response.css('.listnews a::attr(href)').extract()
        #/baike/1037.html
        for t in t_url:
            text_url=urljoin(base_url,t)
            #'http://www.cpic.com.cn'+'/baike/1037.html'
            yield Request(text_url,callback=self.get_text)


    def get_text(self,response):
        info=itm()
        info['title']=response.css('h2>a::text').extract()
        #response.xpath("//div[@class="bxmian"]/div[@class="bx_l"]/div[@class="citiao"]/dl[@class="listmod"]/h2/dt/a/text()").extract()
        info['text']=response.css('dd>p::text').extract()
        #response.xpath("//div[@class="bxmian"]/div[@class="bx_l"]/div[@class="citiao"]/dl[@class="listmod"]/dd/p/text()").extract()
        return info

