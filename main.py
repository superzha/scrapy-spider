# -*- coding:utf-8 -*-

'''
把main脚本作为启动scrapy项目入口（sys的execute方法将scrapy启动命令传入），
以达到用debug模式启动scrapy项目的目的，如此便能对项目断点调试
'''
from scrapy.cmdline import execute

import sys
import os

'''
通过os获取当前路径
'''
# print('current_path:'+os.path.abspath(__file__))
'''
通过os获取项目路径（main的父级路径）
'''
# print('project_path:'+os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'institution'])
