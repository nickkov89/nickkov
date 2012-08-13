from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from tweetplay.models import *
import urllib2, urllib


def index(request):
	song = insertAndReturnRecentSong()
	song = urllib.urlencode({'q':song})
	result = urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?'+song+'&max-results=3&alt=json')
	content = result.read()
	return render_to_response('tweetplay/index.html', {"content":content}, context_instance=RequestContext(request))