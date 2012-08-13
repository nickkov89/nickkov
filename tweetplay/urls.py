from django.conf.urls import patterns, include, url
from tweetplay import views

urlpatterns=patterns('tweetplay.views',
    url(r'^$','index'),
)