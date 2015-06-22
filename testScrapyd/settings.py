# -*- coding: utf-8 -*-

# Scrapy settings for testScrapyd project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'testScrapyd'

SPIDER_MODULES = ['testScrapyd.spiders']
NEWSPIDER_MODULE = 'testScrapyd.spiders'

EMAIL_LIST=[
    'h1@1.com'
    ,'h2@1.com'
    ,'h3@1.com'
    ,'h4@1.com']
PASSWORD_LIST=[
    'h1'
    ,'h2'
    ,'h3'
    ,'h4'
]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'testScrapyd (+http://www.yourdomain.com)'
