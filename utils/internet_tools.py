# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:57:39 2021

@author: ert
"""
import time

import requests

from private.private_info import mq_list, dispatch_address
from utils.datetime_tools import get_time_tag


def hey_probius(city, cooked_list):
    unique_titles = []
    for each in cooked_list:
        title = each.select('td > a')[0]['title']
        if title in unique_titles:
            continue
        else:
            unique_titles.append(title)
            
        for i in mq_list:
            requests.post(
                dispatch_address,
                data = {
                    'to': i,
                    'link': each.select('td > a')[0]['href'],
                    'text': '|'.join([city, title, get_time_tag(each)])
                    }
                )
            time.sleep(0.2)