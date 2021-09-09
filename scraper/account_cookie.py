# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:06:07 2021

@author: ert
"""
import json

from scraper.browser import generate_clean_browser
from config.static_vars import cookies_path

browser = generate_clean_browser()
# TODO: some automatic script to get rid of anti-scrape verifications
# 1. click that stupid hover tab
# 2. send keys
# 3. slide that knot

fresh_cookies = browser.get_cookies()
with open(cookies_path, 'w') as f:
    json.dump(fresh_cookies, f)


def generate_new_cookies():
    pass
