# -*- coding: utf-8 -*-
import scrapy
from job_china.items import JobChinaItem
import time
import random
class A51jbSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    global page
    page=2
    def parse(self, response):
        global page
        job_list = response.xpath("//div[@class='el']")
        for job in job_list:
            if job.xpath(".//p//a[@target='_blank']/@title").extract_first() is not None:
                item = JobChinaItem()
                item["name"]=job.xpath(".//p//a[@target='_blank']/@title").extract_first()
                item["campany_name"]=job.xpath(".//span[@class='t2']/a[@target='_blank']/@title").extract_first()
                item["work_position"] = job.xpath(".//span[@class='t3']/text()").extract_first()
                item["salary"] = job.xpath(".//span[@class='t4']/text()").extract_first()
                item["time"]=job.xpath(".//span[@class='t5']/text()").extract_first()

                html=job.xpath(".//p//a[@target='_blank']/@href").extract_first()
                yield scrapy.Request(
                    html,
                    callback=self.parse_detail,
                    meta={"item": item}
                )
        time.sleep(round(random.uniform(1,3),1))
        next_url ='https://search.51job.com/list/010000,000000,0000,00,9,99,%2B,2,'+str(page)+'.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        page=page+1
        yield scrapy.Request(url=next_url,callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        item["require"]=response.xpath("//p[@class='msg ltype']/@title").extract()
        item["describe"]=response.xpath("//span[@class='sp4']/text()").extract()
        item["type"] = response.xpath("//a[@class='el tdn']/text()").extract()
        yield item
