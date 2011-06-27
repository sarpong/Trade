from django.db import models
from django.contrib import admin

class Advert(models.Model):
	Item=models.CharField(max_length=100)
	name=models.CharField(max_length=60)
	price=models.FloatField()
	phone=models.CharField(max_length=100)
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	def __unicode__(self):
	    return self.Item+ " , $"+str(self.price)+" ," +str(self.updated)

class Request(models.Model):
	product=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	phone=models.CharField(max_length=100)
	email=models.EmailField()
	def __unicode__(self):
	    return self.product+" , "+str(self.updated)

class AdvertAdmin(admin.ModelAdmin):
       list_display=('Item','name','price','phone','email','created')
       list_filter=('Item','created','name')
       search_fields=('name','Item')
       ordering=('Item','created')

class RequestAdmin(admin.ModelAdmin):
      list_display=('product','created','phone','email')
      ordering=('product','-created')

admin.site.register(Advert,AdvertAdmin)
admin.site.register(Request,RequestAdmin)

