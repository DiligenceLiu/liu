# coding=utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from models import *
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from goods.models import *


# 注册页面
def zhuce(request):
    return render(request, 'tiantian/register.html')

# 注册页面处理
def zhuce_handle(request):
    post = request.POST
    # 接收用户输入

    # 采用.get/request.POST['']
    uname = post['user_name']
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否一致
    if upwd != upwd2:
        return redirect('/user/zhuce/')
    # 对密码进行加密
    spwd = sha1()
    spwd.update(upwd)
    upwd3 = spwd.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #转到登录页面
    return redirect('/user/login/')

# 检查用户名是否已经被注册
def zhuce_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname = uname).count()
    return JsonResponse({'count':count})

# 登录页面
def login(request):
    uname = request.COOKIES.get('name','')
    context = {'error_name':1,'error_pwd':1,'uname':uname}
    return render(request, 'tiantian/login.html', context)

# 登录页面处理
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('yes',0)
    user = UserInfo.objects.filter(uname = uname) #[]
    if len(user)!=0:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == user[0].upwd:
            url = request.COOKIES.get('url','/goods/')
            redirect1 = HttpResponseRedirect(url)
            if remember != 0:
                redirect1.set_cookie('name',uname)
            else:
                redirect1.set_cookie('name','',max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = uname
            return redirect1
        else:
            context = {'error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}

            return render(request, 'tiantian/login.html', context)
    else:
        context = {'error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
        return render(request, 'tiantian/login.html',context)


# 用户中心
@user_decorator.login
def user_center_info(request):
    uname = request.session['user_name']
    uemail = UserInfo.objects.get(id=request.session['user_id']).uemail
    uaddress = UserInfo.objects.get(id=request.session['user_id']).uaddress
    uphone = UserInfo.objects.get(id=request.session['user_id']).uphone

    # 最近浏览
    ids = request.COOKIES.get('ids','')
    ids1 = ids.split(',')
    # list = GoodsInfo.objects.filter(id__in=ids1)
    list = []
    for i in ids1:
        if i == '':
            pass
        else:
            list.append(GoodsInfo.objects.get(id=int(i)))
    context = {'uname':uname,'uemail':uemail,'uaddress':uaddress,'uphone':uphone,'list':list}
    return render(request,'tiantian/user_center_info.html',context)

# 订单详情
@user_decorator.login
def user_center_order(request):
    return render(request,'tiantian/user_center_order.html')


# 收货地址
@user_decorator.login
def user_center_site(request):
    user = UserInfo.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushouname = post.get('shoujianren')
        user.uaddress = post.get('dizhi')
        user.uyoubian = post.get('youbian')
        user.uphone = post.get('phone')
        user.save()
    context = {'user':user}
    return render(request,'tiantian/user_center_site.html',context)

# 退出用户
def out(request):
    #清空session
    request.session['user_name'] = ''
    del request.session['user_id']
    return redirect('/goods/')










