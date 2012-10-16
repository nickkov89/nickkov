from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class University(models.Model):
	name = models.CharField(max_length=50)
	is_active = models.BooleanField(default=0)
		
	def __unicode__(self):
		return self.name

class Community(models.Model):
	name = models.CharField(max_length=50)
	university = models.ForeignKey(University)

	def __unicode__(self):
		return self.name

class Building(models.Model):
	name = models.CharField(max_length=35)
	community = models.ForeignKey(Community)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	accepted_eula = models.BooleanField()
	room_number = models.CharField(max_length=5)
	building = models.ForeignKey(Building)
	community = models.ForeignKey(Community)
	is_private = models.BooleanField(default=0)
	is_ra = models.BooleanField()
	belongs_to = models.ForeignKey('self', null=True)
	is_rd = models.BooleanField()
	favorite_movies = models.TextField()
	favorite_books = models.TextField()
	favorite_music = models.TextField()

	def __unicode__(self):
		return self.user.username

	def getInfractions(self):
		return Infraction_Meta.objects.filter(given_to=self.id)	

	def getRA(self):
		if self.is_ra == 0:
			return self.belongs_to.user.id
		else:
			return 0

	def getStudents(self):
		if self.is_ra == 1:
			return UserProfile.objects.filter(belongs_to=self.id)

	def getStudentsInBuilding(self):
		return UserProfile.objects.filter(building_id = self.building_id).filter(~Q(pk=self.id))

	@models.permalink
	def get_absolute_url(self):
		return ('user', (), {'user_id': self.id,})

	#returns all messages by RA
	def getEventsByRA(self, limit):
		return Event.objects.filter(posted_by = self.getRA())[:limit]

class Message(models.Model):
	title = models.CharField(max_length=300)
	content = models.TextField()
	is_active = models.BooleanField(default=0)
	importance_level = models.IntegerField()
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	slug = models.SlugField(null=True)
	to = models.ForeignKey(UserProfile, null=True)
	posted_by = models.ForeignKey(UserProfile, null=True, related_name='from')

class Event(Message):
	where = models.CharField(max_length=60)
	when = models.DateField()

	def __unicode__(self):
		return self.title

class Infraction(models.Model):
	type = models.CharField(max_length=25)

class Infraction_Meta(models.Model):
	type = models.ForeignKey(Infraction)
	when = models.DateField()
	given_by = models.ForeignKey(UserProfile)
	given_to = models.ForeignKey(UserProfile, related_name='infracted_user')

	def __unicode__(self):
		return "given_by: " + self.given_by.user.username + " given to: " + self.given_to.user.username


