# coding=utf-8
from django.db import models


class OrderInfo(models.Model):
    # 用户id
    uid = models.ForeignKey('dayday.UserInfo')
    # 订单编号
    oid = models.CharField(max_length=20,primary_key=True)
    time = models.DateTimeField(auto_now=True)
    isPay = models.BooleanField(default=False)
    address = models.CharField(max_length=200,default='')
    # 总金额
    total = models.DecimalField(max_digits=6, decimal_places=2)

# 订单详情页
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()