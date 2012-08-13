from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login


def index(request):
	return render_to_response("trackme/index.html", context_instance=RequestContext(request))


def login(request):
	if request.method == "POST":		
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			print "good"
		else:
			print "bad"
		return render_to_response("trackme/index.html", context_instance=RequestContext(request))
	else:
		pass
