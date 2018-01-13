from django.contrib import admin
from models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle','gimage','gprice','gjianjie','isDelete','gunit','gclick','gnumber','gjieshao','gtype']
    list_per_page = 15

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
