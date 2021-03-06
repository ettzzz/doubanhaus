# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:06:00 2021

@author: ert
"""

import time
import re
from urllib.parse import unquote

from bs4 import BeautifulSoup

from utils.data_tools import random_tose, post_filter_pipeline
from config.static_vars import headers


def get_group_urls(session, keyword, page_limit = 3):
    ss = session
    base_url = 'https://www.douban.com/search'
    params = {
        'cat': 1019,
        'q': keyword,
        'start': 0
        }
    
    gonna_hit = []
    for i in range(page_limit):
        r = ss.get(base_url, params=params, headers=headers)
        time.sleep(random_tose() + 1)
        soup = BeautifulSoup(r.text, 'html.parser')
        groups = soup.select('div.result-list > div.result > div.content')
        for g in groups:
            try:
                href = g.select('h3 > a')[0]['href']
                group_href = re.findall(r'url=(.*?)&query', unquote(href))
                member_count = int(g.select('div.info')[0].get_text().strip().split(' ')[0])
                if member_count >= 20000:
                    gonna_hit += group_href
            except:
                continue

    real_gonna_hit = list(set(gonna_hit))
    ss.close()
    return real_gonna_hit


def get_posts(session, city, group_url):
    ss = session
    checked = []
    for page in range(3):
        base_url = group_url + 'discussion'
        params = {'start': page*25}
        r = ss.get(base_url, params=params, headers=headers)
        time.sleep(random_tose() + 1)
        
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.select('table.olt > tr')[1:]
        checked += post_filter_pipeline(city, posts)
    ss.close()
    return checked