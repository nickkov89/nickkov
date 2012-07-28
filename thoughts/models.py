from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Entry(models.Model):
	title = models.CharField(max_length=300)
	content = models.TextField()
	is_active = models.BooleanField(default=0)
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	slug = models.SlugField(null=True)

	def __unicode__(self):
		return self.content

	@models.permalink
	def get_absolute_url(self):
		return ('entry', (), {'slug': self.slug, 'entry_id': self.id,})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Entry, self).save(*args, **kwargs)


class Comment(models.Model):
	entry = models.ForeignKey('Entry')
	by = models.CharField(max_length=20)
	content = models.TextField()
	is_active = models.BooleanField(default=0)
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)

	def __unicode__(self):
		return self.content