from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from forum.models import Topic, TopicOverdue, TopicHide
from lxml import etree, html
import requests
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Get Ads'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'}

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.PushCountAdvert()

    def PushCountAdvert(self):
        hide_adds = TopicHide.objects.filter(user=2).values('ads_item')
        oeverdue_ads = TopicOverdue.objects.filter(user=2).values('ads_item')
        list_ads =  Topic.objects.exclude(id__in=hide_adds)

        delta = datetime.now() - timedelta(hours=5)
        list_ads = list_ads.filter(time_parsing__gte=delta).exclude(id__in=oeverdue_ads)
        session = requests.Session()
        session.headers = self.headers
        datetimeThis = datetime.now()
        session.get("https://pushall.ru/api.php?type=broadcast&id=2282&key=9165ef43d6e7cf04660ef95348579c17&title=%s&text=%s" % (datetimeThis, 'Тем с форумов - ' + list_ads.count()))