from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [

	#list of posts
	url(r'^$', views.post_list, name ='post_list'),

	#details of post + comments
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name ='post_detail'),

	#adding post
	url(r'^post/new/$', views.post_add, name='post_add'),

	#publishing post
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

	#draft posts
	url(r'^draft_posts$', views.post_drafts, name='post_drafts'),

	#editing post
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

	#removing post
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

	#removing comment
	url(r'^post/(?P<pk>\d+)/comment_remove/$', views.comment_remove, name='comment_remove'),

]