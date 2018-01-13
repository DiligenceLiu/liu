from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^carts/$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^change(\d+)_(\d+)/$',views.change),
    url(r'^delete(\d+)/$',views.delete),
]