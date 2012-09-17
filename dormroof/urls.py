from django.conf.urls import patterns, include, url
from dormroof import views

urlpatterns=patterns('dormroof.views',
    url(r'^$','login'),
    url(r'^login/$','login'),
    url(r'^index/$','index'),
    url(r'^logout/$','logout'),
    url(r'^browse/$','browse'),
    url(r'^user/(?P<user_id>\d+)/$', 'user',name="user"),
    url(r'^manage/$', 'manage'),
    url(r'^sendMessage/$', 'sendMessage'),
    url(r'^sendEvent/$', 'sendEvent'),
    url(r'^sendEmail/$', 'sendEmail'),

)