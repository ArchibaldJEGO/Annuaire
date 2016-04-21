from django.conf.urls import url
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^home/$', 'liste.views.home'),
    url(r'^form/$', 'liste.views.formulaire'),
    url(r'^delete/(?P<id>\d+)$', 'liste.views.delete'),
    url(r'^edit/(?P<id>\d+)$', 'liste.views.edit'),
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
]
