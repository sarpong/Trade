from django.contrib import admin
from models import Advert, Request

class AdvertAdmin(admin.ModelAdmin):
       list_display=('product','name','price','phone','email','created')
       list_filter=('product','created','name')
       search_fields=('name','product')
       ordering=('product','created')

class RequestAdmin(admin.ModelAdmin):
      list_display=('product','created','phone','email')
      ordering=('product','-created')

admin.site.register(Advert,AdvertAdmin)
admin.site.register(Request,RequestAdmin)

