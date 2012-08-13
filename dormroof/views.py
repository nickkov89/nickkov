from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from dormroof.models import *


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
		if user_info.is_ra == 1:
			pass
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
	user = get_object_or_404(UserProfile, pk=user_id)
	return render_to_response("dormroof/user.html", {'user':user}, context_instance=RequestContext(request))