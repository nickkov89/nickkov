# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from thoughts.models import Comment, Entry

def index(request):
	latest_entries = Entry.objects.filter(is_active=1).order_by('-pub_date')[:5]
	return render_to_response('thoughts/index.html', {'latest_entries':latest_entries}, context_instance=RequestContext(request))

 
def detail(request, entry_id):
	latest_entries = Entry.objects.filter(is_active=1).order_by('-pub_date')[:5]
	entry = get_object_or_404(Entry, pk=entry_id)
	return render_to_response('thoughts/detail.html', {'entry':entry, 'latest_entries':latest_entries}, context_instance=RequestContext(request))