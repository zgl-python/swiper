# 存放所有通用逻辑代码
import re
import random

from django.core.cache import cache
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





