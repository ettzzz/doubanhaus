# -*- coding: utf-8 -*-

import sqlite3
import traceback
from functools import wraps


def sqlite3_pipeline_wrapper(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        conn = self.on()
        results = func(self, *args, **kwargs)
        self.off(conn)
        return results
    return wrapper


class sqliteBaseOperator():
    def __init__(self, db_path):
        self.db_path = db_path


    def on(self):
        conn = sqlite3.connect(self.db_path)
        return conn


    def off(self, conn):
        try:
            conn.commit()
        except:
            traceback.print_exc()
            conn.rollback()
        conn.close()


    def fetch_by_command(self, sql_command):
        conn = self.on()
        result = conn.execute(sql_command).fetchall()
        self.off(conn)
        return result


    def table_info(self, table_name):
        result = self.fetch_by_command(
            "PRAGMA table_info('{}');".format(table_name)
            )
        return result


    def delete_table(self, table_name):
        conn = self.on()
        conn.execute("DELETE FROM '{}';".format(table_name))
        conn.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='{}';".format(table_name))
        self.off(conn)


    def drop_table(self, table_name):
        conn = self.on()
        conn.execute("DROP TABLE '{}';".format(table_name))
        self.off(conn)


    def create_table_sql_command(self, table_name, field_dict):
        field_part = []
        for field_name, addition_list in field_dict.items():
            field_part.append(field_name + ' ' + ' '.join(addition_list))

        sql_command = '''CREATE TABLE IF NOT EXISTS '{}'(\
            uid INTEGER PRIMARY KEY AUTOINCREMENT,\
            {});'''.format(table_name, ','.join(field_part))

        return sql_command


    def insert_batch_sql_command(self, table_name, fields):
        sql_command = "INSERT INTO '{}' ({}) VALUES ({});".format(
            table_name,
            ','.join(fields),
            ','.join(['?']*len(fields)),
            )
        return sql_command


    def add_index_sql_command(self, table_name, index_field):
        sql_command = "CREATE UNIQUE INDEX {} ON '{}' ({});".format(
            index_field + '_index',
            table_name,
            index_field
            )
        return sql_command
