from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.goods),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^detail(\d+)/$', views.detail),


]