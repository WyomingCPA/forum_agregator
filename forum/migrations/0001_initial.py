# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 20:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FreelanceAdsStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_check', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', max_length=300)),
                ('text', models.CharField(help_text=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', max_length=2000)),
                ('site', models.CharField(help_text=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82 \xd0\xbd\xd0\xb0 \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xbc \xd0\xbd\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe \xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0', max_length=200)),
                ('link', models.CharField(help_text=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x83', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TopicHide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_check', models.DateTimeField(auto_now=True)),
                ('topic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicOverdue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_check', models.DateTimeField(auto_now=True)),
                ('topic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='freelanceadsstar',
            name='topic_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic'),
        ),
        migrations.AddField(
            model_name='freelanceadsstar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
