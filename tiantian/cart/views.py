# coding=utf-8
from django.shortcuts import render,redirect
from dayday import user_decorator
from models import *
from django.http import JsonResponse

# 购物车
@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = Cart.objects.filter(cuser_id=uid)
    context = {'carts':carts}
    return render(request,'cart/cart.html',context)

# 向购物车中添加商品
@user_decorator.login
def add(request,gid,count):
    #uid买了count个gid商品
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = Cart.objects.filter(cuser_id=uid,cgoods_id=gid)
    if len(carts) > 0:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = Cart()
        cart.cuser_id = uid
        cart.cgoods_id = gid
        cart.count = count
    cart.save()
    if request.is_ajax():
        count = Cart.objects.filter(cuser_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/carts/')

#手动修改购物车商品数量
@user_decorator.login
def change(request,cart_id,count):
    try:
        cart = Cart.objects.get(id=int(cart_id))
        cart.count = int(count)
        cart.save()
        data = {'ok':0}
    except Exception as e:
        data = {'ok':cart.count}
    return JsonResponse(data)

#删除购物车商品
@user_decorator.login
def delete(request,id):
    try:
        cart = Cart.objects.get(id=int(id))
        cart.delete()
        shuju = {'ok':1}
    except Exception as e:
        shuju = {'ok':0}
    return JsonResponse(shuju)









