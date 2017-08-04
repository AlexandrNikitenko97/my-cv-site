from django.conf.urls import url
from . import views


app_name = 'main'

urlpatterns = [
	url(r'^$', views.home , name = "home" ),
	url(r'^about_me/$', views.about_me , name = "about_me" ),
]