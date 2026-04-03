import os
from celery import Celery
from workers import config

# 将celery 与django结合在一起使用
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swipe.settings')   # 设置django的环境


celery_app = Celery('worker')          # 创建一个celery_app对象作为worker
celery_app.config_from_object(config)  # 引入celery的配置
celery_app.autodiscover_tasks()        # 自动发现任务