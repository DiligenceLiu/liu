from django.shortcuts import render
from .models import *
from dayday import user_decorator
from dayday.models import *
from cart.models import *


@user_decorator.login
def order(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    shuju = request.GET
    cart_ids = shuju.getlist('cart_id')
    list = []
    for i in cart_ids:
        id1 = int(i)
        list.append(id1)
    carts = Cart.objects.filter(id__in=list)
    # cart_id = [int(i) for i in cart_ids]
    # carts = Cart.objects.filter(id__in=cart_id)
    context = {'user':user,'carts':carts}
    return render(request,'order/place_order.html',context)
