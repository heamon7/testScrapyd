# -*- coding: utf-8 -*-
import scrapy
from testScrapyd import settings
import requests

class ScrapyderSpider(scrapy.Spider):
    name = "scrapyder"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/topic/19776749/questions',
    )
    def __init__(self,spider_type='Master',spider_number=0,partition=1,**kwargs):
        # self.stats = stats
        print "Initianizing ....."
        self.spider_type = spider_type
        self.spider_number = spider_number
        self.partition = partition
        spider_number = int(spider_number)
        partition= int(partition)
        # self.spider_number = spider_number
        # self.spider_number = spider_number
        # leancloud.init(settings.APP_ID_S, master_key=settings.MASTER_KEY_S)
        # client1 = bmemcached.Client(settings.CACHE_SERVER_1,settings.CACHE_USER_1,settings.CACHE_PASSWORD_1)
        # client2 = bmemcached.Client(settings.CACHE_SERVER_2,settings.CACHE_USER_2,settings.CACHE_PASSWORD_2)
       # redis0 = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_USER+':'+settings.REDIS_PASSWORD,db=0)
        self.email= settings.EMAIL_LIST[int(spider_number)]
        self.password=settings.PASSWORD_LIST[int(spider_number)]
        # self.questionIdList = redis0.hvals('questionIndex')
        # questionIdListLength = len(self.questionIdList)
        self.questionIdList= range(0,123)
        questionIdListLength =123
        if spider_type=='Master':
            if int(partition)!=1:
                self.questionIdList = self.questionIdList[int(spider_number)*questionIdListLength/partition:(int(spider_number)+1)*questionIdListLength/partition]
                for index in range(1,int(spider_number)):
                    payload ={
                        'project':settings.BOT_NAME
                        ,'spider':self.name
                        ,'spider_type':'Slave'
                        ,'spider_number':index
                        ,'partition':int(partition)
                        ,'settings':'JOBDIR=/tmp/scrapy/scrapyder'+str(index)
                    }
                    response = requests.post(settings.SCRAPYD_HOST+'schedule.json',data=payload)

        elif spider_type =='Slave':
            if int(partition)-int(spider_number)!=1:
                self.questionIdList = self.questionIdList[int(spider_number)*questionIdListLength/partition:(int(spider_number)+1)*questionIdListLength/partition]
            else:
                self.questionIdList = self.questionIdList[int(spider_number)*questionIdListLength/partition:]

    def parse(self, response):
        print "spider_type: %s\nspider_number: %s\npartition: %email: %s\npassword: %s\nquestionIdList: %s" % (self.spider_type
                                                                                                               ,self.spider_number
                                                                                                               ,self.partition
                                                                                                               ,self.email
                                                                                                               ,self.password
                                                                                                               ,str(self.questionIdList))
        pass
