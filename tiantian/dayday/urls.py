# coding=utf-8
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^zhuce/$',views.zhuce),
    url(r'^zhuce_handle/$', views.zhuce_handle),
    url(r'^zhuce_exist/$', views.zhuce_exist),
    url(r'^login_handle/$', views.login_handle),
    url(r'^login/$', views.login),
    url(r'^user_center_info/$',views.user_center_info),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^out/$', views.out),
]