from django.conf.urls import url 
from . import views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.portfolio_list, name='portfolio_list'),
    url(r'^details/(?P<pk>\d+)/$', views.portfolio_details, name='portfolio_details'),
    url(r'^web/$', views.portfolio_web, name='portfolio_web'),
    url(r'^program/$', views.portfolio_programs, name='portfolio_programs'),
    url(r'^bots/$', views.portfolio_bots, name='portfolio_bots'),
    url(r'^mobile_apps/$', views.portfolio_mobile_apps, name='portfolio_mobile_apps'),
    url(r'^add_project/$', views.portfolio_add_project, name='portfolio_add_project'),
    url(r'^delete/(?P<pk>\d+)/$', views.portfolio_delete_project, name='portfolio_delete_project'),
    url(r'^edit/(?P<pk>\d+)/$', views.portfolio_edit_project, name='portfolio_edit_project')
]