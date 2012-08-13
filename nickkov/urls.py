from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^thoughts/', include('thoughts.urls')),
    url(r'^trackme/', include('trackme.urls')),
    url(r'^dormroof/', include('dormroof.urls')),
    url(r'^tweetplay/', include('tweetplay.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
