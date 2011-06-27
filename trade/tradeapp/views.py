# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from tradeapp.models import Advert, Request
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout

class AdvertForm(ModelForm):
	class Meta:
		model = Advert
		exclude=['post']

class RequestForm(ModelForm):
	class Meta:
		model = Request
		exclude=['post']

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

def advert_list(request, limit=100):
	advert_list = Advert.objects.all()
	t = loader.get_template('trade/adlist.html')
	c = Context({'advert_list':advert_list})
	return HttpResponse(t.render(c))

def request_list(request, limit=100):
	request_list = Request.objects.all()
	t = loader.get_template('trade/reqlist.html')
	c = Context({'request_list':request_list})
	return HttpResponse(t.render(c))

def search(request, term):
	advert_list = Advert.objects.filter(Item__icontains=term)
	for advert in advert_list:
		if term == advert:
			print advert.id, advert.product, advert.name, advert.price, advert.phone, advert.email, advert.updated
		else:
			print 'No advert found on product required.'
	f = loader.get_template('trade/search.html')
	g = Context({'advert_list':advert_list,'term':term})
	return HttpResponse(f.render(g))

def home(request):
	t = loader.get_template('trade/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

