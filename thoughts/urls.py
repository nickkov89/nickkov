from django.conf.urls import patterns, include, url

urlpatterns = patterns('thoughts.views',
    url(r'^$','index'),
    url(r'^entry/(?P<entry_id>\d+)/$','detail'),
)