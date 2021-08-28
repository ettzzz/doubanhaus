# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:02:06 2021

@author: ert
"""

import os
import json

import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from config.static_vars import ROOT, OS


def generate_clean_browser():
    init_url = 'https://www.douban.com'
    options = Options()
    options.add_argument('--headless')
    options.log.level = 'fatal'
    
    if OS == 'Windows':
        gecko_bin = 'geckodriver.exe'
    else:
        gecko_bin = 'geckodriver'
        
    browser = Firefox(
        executable_path = os.path.join(ROOT, gecko_bin), 
        options=options)
    
    browser.get(init_url)
    return browser


def generate_browser_with_cookies():
    browser = generate_clean_browser()
    with open(os.path.join(ROOT, 'private', 'cookies.txt'), 'r') as f:
        cookies = json.load(f)
    for c in cookies:
        browser.add_cookie(c)
    return browser


def generate_session_with_cookies():
    sess = requests.session()
    with open(os.path.join(ROOT, 'private', 'cookies.txt'), 'r') as f:
        cookies = json.load(f)
    sess_cookies = dict()
    for c in cookies:
        sess_cookies[c['name']] = c['value']

    sess.cookies = requests.utils.cookiejar_from_dict(sess_cookies) 
    return sess
    


