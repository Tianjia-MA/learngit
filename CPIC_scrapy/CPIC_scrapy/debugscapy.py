from scrapy.cmdline import execute
import os
import sys

dirpath=os.path.dirname(os.path.abspath(__file__))
#print(dirpath)

#环境变量
sys.path.append(dirpath)

#execute scrapy
execute(['scrapy','crawl','cpic_scrapy'])