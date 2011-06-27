from django.db import models
from django.contrib import admin

class Advert(models.Model):
	product=models.CharField(max_length=100)
	name=models.CharField(max_length=60)
	price=models.FloatField()
	phone=models.CharField(max_length=100)
	email=models.EmailField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	def __unicode__(self):
	    return self.product+ " , $"+str(self.price)+" ," +str(self.updated)

class Request(models.Model):
	product=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	phone=models.CharField(max_length=100)
	email=models.EmailField()
	def __unicode__(self):
	    return self.product+" , "+str(self.updated)

