# -*- encoding: utf-8 -*-

# python apps
from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')


# 注册Celery的APP
celery_app = Celery()
# 绑定配置文件
celery_app.config_from_object('django.conf:settings', namespace='CELERY')


# 自动发现各个app下的tasks.py文件
celery_app.autodiscover_tasks()
