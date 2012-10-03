from django.shortcuts import render_to_response
from django.template import RequestContext
from mapit import APP_NAME

def index(request):
	results = ArticleUtil.getArticlesByQuery('drugs')

	return render_to_response("mapit/index.html", {"APP_NAME" : APP_NAME, "results" : results}, context_instance=RequestContext(request))