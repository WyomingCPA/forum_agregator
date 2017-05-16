# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

#Модель объявления
class Topic(models.Model):
    title = models.CharField(max_length=300, help_text='Заголовок темы')
    text = models.CharField(max_length=2000, help_text='Текст темы')
    site = models.CharField(max_length=200, help_text='Сайт на котором найдено тема')
    link = models.CharField(max_length=200, help_text='Ссылка на тему')
    time_parsing = models.DateTimeField(auto_now = True, help_text='Время добавления в БД')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/topic/%i/" % self.id

#Скрыть объявления 
class TopicHide(models.Model):
    user = models.ForeignKey(User)
    topic_item = models.ForeignKey(Topic)
    time_check = models.DateTimeField(auto_now = True)

#Просроченные объявления
class TopicOverdue(models.Model):
    user = models.ForeignKey(User)
    topic_item = models.ForeignKey(Topic)
    time_check = models.DateTimeField(auto_now = True)

#Избранные объявления
class FreelanceAdsStar(models.Model):
    user = models.ForeignKey(User)
    topic_item = models.ForeignKey(Topic)
    time_check = models.DateTimeField(auto_now = True)
