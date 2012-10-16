from django.conf.urls import patterns, include, url
from mapit import views

urlpatterns=patterns('mapit.views',
    url(r'^$','index'),
)