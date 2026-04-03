#!/usr/bin/env python

import os
import sys
import random

import django

# 设置环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swipe.settings")
django.setup()

from user.models import User
# from vip.models import Vip, Permission, VipPermRelation



last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'

)


first_names = {
    'male': [
        '致远', '俊驰', '雨泽', '烨磊', '晟睿',
        '天佑', '文昊', '修洁', '黎昕', '远航',
        '旭尧', '鸿涛', '玮琪', '荣轩', '越泽',
        '浩宇', '景瑜', '浩轩', '普泽', '绍辉',
        '邵琪', '盛荣', '盛杰', '盛迪', '思聪',
        
    ],

    'female': [
        '佩玲', '欣妍', '佳琪', '雅芙', '雨停',
        '蕴涵', '黎姿', '玉婷', '凝心', '妙玲',
        '欣琪', '文苑', '诗婧', '陆洁', '婧麒',
        '亚玲', '灵韵', '清寒', '融悦', '苏菲',
        '宇佳', '雅静', '梦洁', '梦露', '慧倩',
    ]
}

# 生成性别 名字
def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex


def cerate_robots(n):
    # 创建新用户

    for i in range(n):
        name ,sex = random_name()
        try:
            User.objects.create(
                phonenum = '%s' % random.randrange(21000000000, 21900000000),
                nickname = name,
                sex = sex,
                birth_year = random.randint(1980, 2000),
                birth_month = random.randint(1, 12),
                birth_day = random.randint(1, 28),
                location = random.choice(['bj', 'sh', 'gz', 'sz', 'cd', 'xa', 'wh']),
            )
            print('created:%s %s'% (name, sex))
        except django.db.utils.IntegrityError:
            pass


if __name__ == '__main__':
    cerate_robots(5000)
