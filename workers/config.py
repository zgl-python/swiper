# celery的配置文件

# 中间者的url 这里是以redis作为中间者
broker_url = 'redis://127.0.0.1:6379/1'
broker_pool_limit = 100   # Broker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'

result_backend = 'redis://127.0.0.1:6379/1'
result_serializer = 'pickle'
result_cache_max = 1000  # 任务结果最大缓存数量
result_expires = 3600  # 任务过期时间

# worker的日志级别
worker_redirect_stdouts_level = 'INFO'