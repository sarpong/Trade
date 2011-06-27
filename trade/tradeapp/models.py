from django.db import models

# Create your models here.

class Advert(models.Model):
	prodName=models.CharField(max_length=100)
	name=models.CharField(max_length=60)
	price=models.FloatField()
	phone=models.CharField()
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	def __unicode__(self):
	    return self.prodName+ " , "+self.price+" ," +str(self.Updated)

class Request(models.Model):
	product=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	phone=models.CharField()
	email=models.EmailField()
	def __unicode__(self):
	    return self.product+" , "+str(self.Updated)

class AdvertAdmin(admin.ModelAdmin):
       list_display=('prodName','name','price','phone','email','created')
       list_filter=('prodName','created','name')
       search_fields=('name','prodName')
       ordering=('prodName','created')

class RequestAdmin(admin.modelAdmin):
      list_display=('product','created','phone','email')
      ordering=('product','-created')

admin.site.register(Advert,AdvertAdmin)
admin.site.register(Request, RequestAdmin)
	
