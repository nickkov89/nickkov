from django.conf.urls import patterns, include, url
from thoughts import views

urlpatterns=patterns('trackme.views',
    url(r'^$','index'),
)