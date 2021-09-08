# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:03:52 2021

@author: ert
"""

import os

from .base_operator import sqliteBaseOperator
from config.static_vars import ROOT
from utils.datetime_tools import get_today_date

class DoubanhausDatabase(sqliteBaseOperator):
    def __init__(self, sql_dbfile_path=os.path.join(ROOT, 'rooms.db')):
        self.sql_dbfile_path = sql_dbfile_path
        self.init_tables = {
            'pool': 'pool',
        }
        self.fields = {
            'pool': {
                'dbid': ['TEXT'],
                'userid': ['TEXT'],
                'city': ['TEXT'],
                'senddate': ['DATE']
            }
        }

        if not os.path.exists(sql_dbfile_path):
            super().__init__(sql_dbfile_path)
            conn = self.on()
            for table in self.init_tables:
                conn.execute(
                    self.create_table_sql_command(
                        self.init_tables[table],
                        self.fields[table])
                )
            self.off(conn)
        else:
            super().__init__(sql_dbfile_path)


    def insert(self, fetched):
        table_name = self.init_tables['pool']
        fields = list(self.fields[table_name].keys())

        conn = self.on()
        conn.executemany(
            self.insert_batch_sql_command(table_name, fields), fetched
        )
        self.off(conn)


    def remove_spam(self, city, posts):
        clean_posts = []
        fill = []
        for each_post in posts:
        # post_pool = get_filter_pool() 
        # TODO: this func will be completed as a loose end after cookie scraper
            post_uid = each_post.select('td > a')[0]['href'].split('/')[-2]
            user_uid = each_post.select('td > a')[1]['href'].split('/')[-2]
            date = each_post.select('td.time')[0].get_text().split(' ')[0]
            year = get_today_date()[:4]
        
            fetch = self.fetch_by_command(
                "SELECT uid FROM {} WHERE dbid='{}' AND city='{}';".format(
                    self.init_tables['pool'],
                    post_uid,
                    city
                    )
                )
            if fetch: # douban抽风 之前的又被刷出来了
                continue
            else:
                senddate = year + '-' + date
                clean_posts.append(each_post)
                fill.append((post_uid, user_uid, city, senddate))
                
        self.insert(fill)
        return clean_posts
        
        # def get_filter_pool():
#     today_str = get_today_date()
#     last_week_str = get_delta_date(today_str, -7)

#     pool = db.fetch_by_command(
#         "SELECT uid, dbid, userid FROM pool WHERE senddate BETWEEN {} AND {};".format(last_week_str, today_str)
#         )

#     return pool