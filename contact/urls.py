from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
	url(r'^$', views.contact , name = "contact" ),
	url(r'^messages/$', views.message_list , name = "message_list" ),
	url(r'^messages/(?P<pk>\d+)/$', views.message_detail , name = "message_detail" ),
	url(r'^messages/delete/(?P<pk>\d+)/$', views.message_delete , name = "message_delete" ),
]