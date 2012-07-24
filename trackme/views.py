from django.shortcuts import render_to_response

def index(request):
	return render_to_response("trackme/index.html", {"lol":2})