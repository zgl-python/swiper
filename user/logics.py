# 存放所有通用逻辑代码
import re
import random
import os

from django.core.cache import cache
from django.conf import settings
from common import keys


def is_phonenum(phonenum):
    '''检查是否是一个正常的手机号'''
    if re.match(r'1[3456789]\d{9}$', phonenum):
        return True
    else:
        return False
    
def gen_random_code(length=4):
    '''产生一个指定长度的随机码'''
    # 看是生成几位的随机码
    rand_num = "%%0%sd" % length   #   第一个%是为了防止第二个%转义
    #   即产生的字符串是  "%04d"
    v_code = rand_num % random.randrange(0, 10 ** length)
    return v_code

def send_sms(phonenum, v_code):
    """发送短信"""
    # print(v_code)
    return v_code
    
def send_vcode(phonenum):
    '''发送验证码'''
    v_code = gen_random_code(6)    # 产生一个随机的验证码
    print('----------->', v_code)
    response = send_sms(phonenum, v_code)    # 发送验证码
    key = keys.VCODE_KEY % phonenum
    cache.set(key, v_code, 180)     # 将验证码放到缓存中
    return True


def save_upload_file(uid, upload_file):
    """保存上传的形象图片"""
    filename = "avatar_%s.png" % uid
    full_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    print(full_path)
    for chunk in upload_file.chunks():
        with open(full_path, "wb+") as fp:
            fp.write(chunk)
    return filename, full_path
        


import time
from workers import celery_app



# 使用装饰器的方式引入celery, 将add函数作为一个任务
@celery_app.task
def add_to(x, y, z):
    time.sleep(5)
    return x+y+z




