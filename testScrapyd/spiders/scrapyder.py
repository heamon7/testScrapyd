# -*- coding: utf-8 -*-
import scrapy
from scrapyd_api import ScrapydAPI

class ScrapyderSpider(scrapy.Spider):
    name = "scrapyder"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/topic/19776749/questions',
    )
    def __init__(self,spider_type='Master',spider_number=0,partition=1,emailList=['hea@163.com'],passwordList=['hea'],**kwargs):
        # self.stats = stats
        print "Initianizing ....."
        scrapyd = ScrapydAPI('http://localhost:6800')
        self.spider_type = spider_type
        self.spider_number = spider_number
        self.partition = partition
        # self.spider_number = spider_number
        # self.spider_number = spider_number
        # leancloud.init(settings.APP_ID_S, master_key=settings.MASTER_KEY_S)
        # client1 = bmemcached.Client(settings.CACHE_SERVER_1,settings.CACHE_USER_1,settings.CACHE_PASSWORD_1)
        # client2 = bmemcached.Client(settings.CACHE_SERVER_2,settings.CACHE_USER_2,settings.CACHE_PASSWORD_2)
       # redis0 = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_USER+':'+settings.REDIS_PASSWORD,db=0)
        dbPrime = 97
        self.email= emailList[0]
        self.password=passwordList[0]
        # self.questionIdList = redis0.hvals('questionIndex')
        # questionIdListLength = len(self.questionIdList)
        self.questionIdList= range(0,123)
        questionIdListLength =123
        if spider_type=='Master':
            if int(spider_number)!=1:
                self.questionIdList = self.questionIdList[int(spider_number)*questionIdListLength/partition:(int(spider_number)+1)*questionIdListLength/partition]
                for index in range(1,int(spider_number)):
                    scrapyd.schedule('zhQuesInfo', 'quesInfoer'

                                     ,spider_type='Slave'
                                     ,spider_number=index
                                     ,partition=partition
                                     ,emailList=[emailList[index]]
                                     ,passwordList=[passwordList[index]]
                                     ,settings='JOBDIR=/tmp/scrapy/zhihu/quesInfoer'+str(index))

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
