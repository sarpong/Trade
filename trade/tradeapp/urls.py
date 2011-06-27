from django.conf.urls.defaults import *
from django.views.generic import list_detail
from trade.tradeapp.models import *

advertise = {
	"queryset": Advert.objects.all(),
}

request = {
	"queryset": Request.objects.all(),
}

urlpatterns = patterns('',
	url(r'^trade/$', list_detail.object_list, advertise),
	url(r'^trade/$', list_detail.object_list, request),
)

