# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv
import itemadapter


class CsvStorePipeline:
    CSV_FILE = None
    CSV_WRITER = None

    @classmethod
    def from_crawler(cls, crawler):
        cls.CSV_FILE = open("../data/book.csv", "w", encoding="utf-8", newline="")
        cls.CSV_WRITER = csv.writer(cls.CSV_FILE)
        row_data = ["price", "name"]
        cls.CSV_WRITER.writerow(row_data)
        print("文件已打开")
        return cls()

    def close_spider(self, spider):
        if CsvStorePipeline.CSV_FILE is not None:
            CsvStorePipeline.CSV_FILE.close()
            print("文件已关闭")

    def process_item(self, item, spider):
        if CsvStorePipeline.CSV_FILE is None:
            CsvStorePipeline.open(CsvStorePipeline)
        adapter = itemadapter.ItemAdapter(item)
        row_data = [adapter["price"], adapter["name"]]
        CsvStorePipeline.CSV_WRITER.writerow(row_data)
        return item
