from django.conf.urls import patterns, include, url

urlpatterns = patterns('thoughts.views',
    url(r'^$','index'),
    url(r'^entry/(?P<slug>[-\w\d]+),(?P<entry_id>\d+)/$','detail',name="entry"),
)