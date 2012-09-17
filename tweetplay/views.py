from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from tweetplay.models import *
import urllib2, urllib
import json


def index(request):
	song = insertAndReturnRecentSong()
	last15 = getLast15()

	historyResults = []
	for somesong in last15:
	 	somesong = urllib.urlencode({'q':somesong})
	 	result = urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?'+somesong+'&max-results=1&alt=json')
	 	content = result.read()
	 	#historyResults.append(content)

	print content

	song = urllib.urlencode({'q':song})
	result = urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?'+song+'&max-results=3&alt=json')
	content = result.read()
	return render_to_response('tweetplay/index.html', {"content":content,'songs':historyResults}, context_instance=RequestContext(request))