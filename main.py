#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 08:21:37 2018

@author: ert
"""

'''
probius:shanghai|title|timer
'''

# import os
import traceback

from utils.internet_tools import hey_probius
from database.haus_operator import DoubanhausDatabase
from scraper.douban_post import get_group_urls, get_posts
from scraper.browser import generate_session_with_cookies
from config.static_vars import city_meta
from gibber import gabber

def main():
    db = DoubanhausDatabase()
    for city, meta in city_meta.items():
        group_word, pages = meta['meta']
        session = generate_session_with_cookies()
        url_list = get_group_urls(session, group_word, pages)
        clean_posts = []
        for each_group in url_list:
            session = generate_session_with_cookies() # is this necessary?
            filtered_posts = get_posts(session, city, each_group)
            clean_posts += db.remove_spam(city, filtered_posts)
        hey_probius(city, clean_posts)
        gabber.info('city: {} with len {}.'.format(city, len(clean_posts)))

if __name__ == '__main__':
    try:
        main()
    except:
        exp = traceback.format_exc()
        gabber.error(exp)
    # os.system("ps aux|grep firefox|awk '{print $2}'|xargs kill -9")
