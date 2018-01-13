# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from cart.models import *


# 商品首页
def goods(request):
    #推荐出最新的4种产品和最热销的4种产品
    list = TypeInfo.objects.all()
    fruit1 = list[0].goodsinfo_set.order_by('-gclick')[0:4]
    fruit2 = list[0].goodsinfo_set.order_by('-id')[0:4]

    shuichan1 = list[1].goodsinfo_set.order_by('-gclick')[0:4]
    shuichan2 = list[1].goodsinfo_set.order_by('-id')[0:4]

    rou1 = list[2].goodsinfo_set.order_by('-gclick')[0:4]
    rou2 = list[2].goodsinfo_set.order_by('-id')[0:4]

    dan1 = list[3].goodsinfo_set.order_by('-gclick')[0:4]
    dan2 = list[3].goodsinfo_set.order_by('-id')[0:4]

    cai1 = list[4].goodsinfo_set.order_by('-gclick')[0:4]
    cai2 = list[4].goodsinfo_set.order_by('-id')[0:4]

    sudong1 = list[5].goodsinfo_set.order_by('-gclick')[0:4]
    sudong2 = list[5].goodsinfo_set.order_by('-id')[0:4]
    context = {'fruit1':fruit1,'fruit2':fruit2,'shuichan1':shuichan1,'shuichan2':shuichan2,'rou1':rou1,'rou2':rou2,'dan1':dan1,'dan2':dan2,'cai1':cai1,'cai2':cai2,'sudong1':sudong1,'sudong2':sudong2}
    return render(request,'goods/index.html',context)

# 商品列表
def list(request,tid,moren,fenye):
    list = TypeInfo.objects.get(pk=int(tid))
    newlist = list.goodsinfo_set.order_by('-id')[0:2]
    goodslist = list.goodsinfo_set.order_by('id')
    #按价格排序
    if moren == '2':
        goodslist = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    if moren == '3':
        goodslist = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    p = Paginator(goodslist,3)
    pagelist = p.page(int(fenye))

    context = {'list': list, 'newlist': newlist, 'pagelist':pagelist,'moren':moren,'p':p,'fenye':fenye}
    return render(request,'goods/list.html',context)

#商品详情页
def detail(request,gid):
    goodsinfo = GoodsInfo.objects.get(pk=int(gid))
    goodsinfo.gclick = goodsinfo.gclick+1
    goodsinfo.save()
    newlist = goodsinfo.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'goodsinfo':goodsinfo,'newlist':newlist}
    response = render(request,'goods/detail.html',context)

    #最近浏览
    ids = request.COOKIES.get('ids','')
    gid = '%d'%goodsinfo.id
    if ids != '':
        ids1 = ids.split(',')
        if ids1.count(gid) > 0:
            ids1.remove(gid)
        ids1.insert(0,gid)
        # if ids1.count() > 5:
        if len(ids1) > 5:
            del ids1[5]
        ids = ','.join(ids1)
    else:
        ids = gid
    response.set_cookie('ids',ids)
    return response













