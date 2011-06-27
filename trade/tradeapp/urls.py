from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$','tradeapp.views.home')
	url(r'^adlist/$', 'tradeapp.views.advert_list'),
	url(r'^reqlist/$', 'tradeapp.views.request_list'),
	url(r'^search/(.*)$','tradeapp.views.search')
#	url(r'^addetail/(?P<id>\d+)/((?P<showAdvert>.*)/)?$','tradeapp.views.advert_detail')
#	url(r'^reqdetail/(?P<id>\d+)/((?P<showRequest>.*)/)?$','tradeapp.views.request_detail')
#	url(r'^logout/$','tradeapp.views.logoutView')
#	url(r'^login$','tradeapp.views.loginView')
#	url(r'^editreq$','tradeapp.views.editreq')
#	url(r'^editadvert$','tradeapp.views.editad')
)

