from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from tweetplay.models import *
import urllib2, urllib
import json


def index(request):
	song = urllib.urlencode({'q':insertAndReturnRecentSong()})
	result = urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?'+song+'&max-results=3&alt=json')

	content = result.read()
	last10 = getLatestSongs(11)[1:11]

	return render_to_response('tweetplay/index.html', {"content":content, "last10":last10}, context_instance=RequestContext(request))