# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from forum.models import Topic
from lxml import etree, html
import requests
import json
import cookielib
import re
import os

import time


class Command(BaseCommand):
    help = 'SearchEngines'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.SearchenginesParser()


    def SearchenginesParser(self):  
        session = requests.Session()
        getNewsPage = session.get("http://searchengines.guru/")
        pageHtml = html.fromstring(getNewsPage.text)
        getAllTitleBlock = pageHtml.xpath(".//*[@class='smallfont']/div[@style]/a")        
        for TitleBlock in getAllTitleBlock:
            try:
               href = TitleBlock.attrib['href']
               RawTitle = TitleBlock.attrib['title']
               title = RawTitle.split("'") 
               link = 'http://searchengines.guru/' + href
               try:
                   Topic.objects.get(link=link)
               except Topic.MultipleObjectsReturned:
                   pass
               except Topic.DoesNotExist:                  
                   itemAds = Topic(title = title[1], site = 'http://searchengines.guru/', link = link)
                   itemAds.save()
            except Exception as e:
               print 'error write to base'




        
