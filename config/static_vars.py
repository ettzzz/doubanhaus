
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:58:50 2021

@author: ert
"""

import os
import platform

OS = platform.system()
OS_VER = platform.version()
ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

if 'Debian' in OS_VER:
    DEBUG = False
else:
    DEBUG = True

LOGGING_FMT = "%(asctime)s %(levelname)s %(funcName)s in %(filename)s: %(message)s"
LOGGING_DATE_FMT = "%Y-%m-%d %a %H:%M:%S"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}

common_stop_words = ['求', '女', '开间', '卧']
common_go_words = ['整租', '一居']

city_meta_template = {
    'city': {
        'go_words': [],
        'stop_words': [],
        'price_range': [0, 0],
        'meta': ('xx租房', 3)
    }
}

city_meta = {
    'beijing': {
        'go_words': common_go_words,
        'stop_words': common_stop_words + ['南法信', '天宫院', '生物医药基地', '花梨坎'],
        'price_range': [3500, 5000],
        'meta': ('北京租房', 3)
    },
    # 'shenzhen': {
    #     'go_words': common_go_words,
    #     'stop_words': common_stop_words,
    #     'price_range': [2500, 5000],
    #     'meta': ('深圳租房', 3)
    # },
}
