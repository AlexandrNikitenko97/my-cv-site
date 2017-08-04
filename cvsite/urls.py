from django.conf.urls import include, url 
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^accounts/login/$', login, {'template_name': 'main/admin/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]

