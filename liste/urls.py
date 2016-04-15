from . import views
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = [
    url(r'^home/$', 'liste.views.home'),
    url(r'^form/$', 'liste.views.personne'),
    url(r'^liste/$', 'liste.views.liste'),
    url(r'^id/(?P<id>\d+)$', 'liste.views.info'),
]
