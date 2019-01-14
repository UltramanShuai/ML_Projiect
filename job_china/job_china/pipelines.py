# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import csv
class JobChinaPipeline(object):

    def open_spider(self,spider):
        global writer
        global c
        c = open("job1.csv", "w")
        writer = csv.writer(c)
        writer.writerow(
            ["Job_name", "Campany", "Salary", "Work_Position", "Post_time","Require","Describe"])


    def process_item(self, item, spider):
        global writer
        global c
        # print(item["name"])
        # print(item["campany_name"])
        # print(item["salary"])
        # print(item["time"])
        # print(item["work_position"])
        print("--------------------------------------------------",item["name"])

        writer.writerow([item["name"],item["campany_name"],item["salary"],item["work_position"],item["time"],str(item["require"]),item["describe"],item["type"]])
        return item
