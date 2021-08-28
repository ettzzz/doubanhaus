# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:57:30 2021

@author: ert
"""
import random
import re

from config.static_vars import city_meta


def random_tose():
    return random.random()


def post_filter_pipeline(city, posts):
    filtered_posts = []
    for each_post in posts:
        title = each_post.select('td > a')[0]['title']
        price = re.findall('\D([\d]{2}00)[\D]?', title)
        # replies = each.select('td')[2].get_text()
        
        if not price:
            continue
        if int(price[0]) < city_meta[city]['price_range'][0] or \
            int(price[0]) > city_meta[city]['price_range'][1]:
            continue
        if any(x in title for x in city_meta[city]['stop_words']):
            continue
        if all(y not in title for y in city_meta[city]['go_words']):
            continue
        filtered_posts.append(each_post)
    
    return filtered_posts


