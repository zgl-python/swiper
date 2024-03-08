from django.db import models

# Create your models here.

class User(models.Model):
    phonenum = models.Field(verbose_name='手机号')
    nickname = models.Field(verbose_name='昵称')
    sex = models.Field(verbose_name='性别')
    birth_year = models.Field(verbose_name='出生')
    birth_month = models.Field(verbose_name='出生')
    birth_day = models.Field(verbose_name='出生')
    avatar = models.Field(verbose_name='手机号')
    location = models.Field(verbose_name='手机号')
    
    