# coding=utf-8
from django.http import HttpResponseRedirect

# 未登录则自动转到登录页面
def login(func):
    def login_func(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            back = HttpResponseRedirect('/user/login/')
            back.set_cookie('url',request.get_full_path())
            return back
    return login_func

# request.get_full_path()  保存get请求的完整路径，包括参数部分和url部分