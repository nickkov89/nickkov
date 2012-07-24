from django.contrib import admin
from thoughts.models import Entry, Comment

admin.site.register(Comment)

class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/admin/js/editor.js',
  )
  css = {
    'all': ('/static/admin/css/editor.css',),
  }

admin.site.register(Entry,
	search_fields = ['title',],
    Media = CommonMedia,
)