# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class CpicScrapyPipeline(object):
    def __init__(self):
        self.file=open("cpic_insurepedia.json",'w',encoding='utf-8')

    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+"\n"
        #ensure_ascii=False解决json中文编码混乱 https://blog.csdn.net/m0_37422289/article/details/82803835
        self.file.write(line)
        return item
