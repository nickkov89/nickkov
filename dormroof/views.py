from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from dormroof.models import *
from django.db import connection
from django.core.mail import EmailMessage



def getUserdata(user_id):
	return UserProfile.objects.get(pk=user_id)

def login(request):
	if request.method == "POST":		
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request,user)
				user_data = UserProfile.objects.get(pk=request.user.id)
				request.session['user_info'] = user_data
				return redirect(index)
			else:
				print "disabled account"
		else:
			return redirect(login)
	elif request.user.is_authenticated():
		return redirect(index)
	else:
		return render_to_response("dormroof/login.html", context_instance=RequestContext(request))

def logout(request):
	auth_logout(request)
	return redirect(login)

def index(request):
	if request.user.is_authenticated():
		user_info = getUserdata(request.user.id)
		url = "index.html"
		return render_to_response("dormroof/index.html", {"user_info": user_info}, context_instance=RequestContext(request))
	else:
		return render_to_response("dormroof/sorry.html", context_instance=RequestContext(request))

def browse(request):
	if request.user.is_authenticated():
		user_info = getUserdata(request.user.id)
		results = UserProfile.objects.get(pk=request.user.id).getStudentsInBuilding()
		return render_to_response("dormroof/browse.html", {"users":results}, context_instance=RequestContext(request))
	else:
		return render_to_response("dormroof/sorry.html", context_instance=RequestContext(request))

def user(request, user_id):
	if request.user.is_authenticated():		
		user = get_object_or_404(UserProfile, pk=user_id)
		return render_to_response("dormroof/user.html", {'user':user}, context_instance=RequestContext(request))
	else:
		return render_to_response("dormroof/sorry.html", context_instance=RequestContext(request))

def manage(request):
	if request.user.is_authenticated() and getUserdata(request.user.id).is_ra == 1:
		return render_to_response("dormroof/manage.html", context_instance=RequestContext(request))
	else:
		return render_to_response("dormroof/sorry.html", context_instance=RequestContext(request))


def sendMessage(request):
	if request.method == "POST":
		message = request.POST.get('message')	
		msg = Message(content = message, importance_level=1, to_id = request.POST.get('user_id'), posted_by_id = request.user.id)
		msg.save()
		return redirect(manage)
	else:
		return render_to_response("dormroof/login.html", context_instance=RequestContext(request))


def sendEvent(request):
	if request.method == "POST":
		where = request.POST.get('where')
		when = request.POST.get('when')
		message = request.POST.get('message')
		event = Event(content = message, importance_level=3, where=where, when=when, posted_by_id=request.user.id)
		event.save()
		return redirect(manage)
	else:
		return render_to_response("dormroof/login.html", context_instance=RequestContext(request))


def sendEmail(request):
	if request.method == "POST":
		email = EmailMessage('Hello', request.POST.get('message'), to=[request.POST.get('user_id')])
		email.send()
		return redirect(manage)
	else:
		return render_to_response("dormroof/login.html", context_instance=RequestContext(request))
























