# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
CREATE DATABASE scrapy;

CREATE TABLE players_data(
   name VARCHAR UNIQUE NOT NULL,
   position VARCHAR NOT NULL,
   height_and_weight VARCHAR NOT NULL,
   team VARCHAR
);
'''

import psycopg2

class NflScrapPipeline:
    db_name = "scrapy"
    db_conn = psycopg2.connect("host=localhost dbname=scrapy user=jothi password=postgres")
    db_cursor = db_conn.cursor()

    def __init__(self):
        #delete previous entries
        self.db_cursor.execute("DELETE FROM players_data")
        self.db_conn.commit()

    def process_item(self, item, spider):
        self.db_cursor.execute("INSERT INTO players_data(name,position,height_and_weight,team)\
                VALUES(%s,%s,%s,%s)", (item['name'], item['position'], item['height_and_weight'], item['team']))
        self.db_conn.commit()

