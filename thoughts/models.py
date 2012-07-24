from django.db import models

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=300)
	content = models.TextField()
	is_active = models.BooleanField(default=0)
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)

	def __unicode__(self):
		return self.content


class Comment(models.Model):
	entry = models.ForeignKey('Entry')
	by = models.CharField(max_length=20)
	content = models.TextField()
	is_active = models.BooleanField(default=0)
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)

	def __unicode__(self):
		return self.content