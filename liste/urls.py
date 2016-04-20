from . import views
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = [
    url(r'^home/$', 'liste.views.home'),
    url(r'^form/$', 'liste.views.formulaire'),
    url(r'^liste/$', 'liste.views.liste'),
]
