# coding=utf-8
from django.db import models

class Cart(models.Model):
    cuser = models.ForeignKey('dayday.UserInfo')
    cgoods = models.ForeignKey('goods.GoodsInfo')
    count = models.IntegerField()
