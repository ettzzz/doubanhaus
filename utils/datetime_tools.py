# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:03:25 2021

@author: ert
"""

import datetime


DATE_FORMAT = "%Y-%m-%d"

def get_time_tag(each):
    now = datetime.datetime.now()
    timestamp = '{}-{}'.format(now.year, each.select('td.time')[0].get_text())
    struct_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    time_gap = now - struct_time

    if time_gap.days >= 1:
        return '一天前'
    elif time_gap.seconds >= 3600:
        hours = time_gap.seconds//3600
        return '{}小时前'.format(hours)
    elif time_gap.seconds >= 60:
        minutes = time_gap.seconds//60
        return '{}分钟前'.format(minutes)
    elif time_gap.seconds >= 10:
        return '{}秒前'.format(time_gap.seconds)
    else:
        return '刚刚'
    
def struct_datestr(datestr, _format=DATE_FORMAT):
    structed_date = datetime.datetime.strptime(datestr, _format)
    return structed_date    

    
def get_today_date():
    today = datetime.datetime.now()
    today_str = datetime.datetime.strftime(today, DATE_FORMAT)
    return today_str


def get_delta_date(date, days):
    '''
    # type(date) is str
    # type(target_datestr) is str
    '''
    strd = struct_datestr(date)
    target_strd = strd + datetime.timedelta(days)
    target_datestr = datetime.datetime.strftime(target_strd, DATE_FORMAT)
    return target_datestr