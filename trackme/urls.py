from django.conf.urls import patterns, include, url
from trackme import views

urlpatterns=patterns('trackme.views',
    url(r'^$','index'),
    url(r'^login/$','login'),
)