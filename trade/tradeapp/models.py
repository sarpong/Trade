from django.db import models

# Create your models here.

class Advert(models.Model):
	prodName=models.CharField(max_length=100)
	name=models.CharField(max_length=60)
	price=models.FloatField()
	phone=models.CharField()
	email=models.EmailField()
	Created=models.DateTimeField(auto_now_add=True)
	Updated=models.DateTimeField(auto_now=True)
	def __unicode__(self):
	    return self.prodName+ " , "+self.price+" ," +str(self.Updated)

class Request(models.Model):
	product=models.CharField(max_length=100)
	Created=models.DateTimeField(auto_now_add=True)
	Updated=models.DateTimeField(auto_now=True)
	phone=models.CharField()
	email=models.EmailField()
	def __unicode__(self):
	    return self.product+" , "+str(self.Updated)



	
