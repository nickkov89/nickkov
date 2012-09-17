from django.db import models
from django.db import connection, transaction
from django.db import DatabaseError

class TweetInfo(models.Model):
	from_user = models.CharField(max_length=20)
	created_at = models.DateTimeField()
	text = models.TextField()

	def __unicode__(self):
		return "from: " + self.from_user + ":    " + self.text


def checkForTwitterFDW():
	cursor = connection.cursor()
	cursor.execute('create extension twitter_fdw')

def getLast15():
	cursor = connection.cursor()

	cursor.execute('SELECT from_user, \
	created_at, \
	text \
	FROM twitter WHERE q=%s and from_user=%s \
	limit 1',
	['bpm_playlist','bpm_playlist'])
	
	rawResults = cursor.fetchall()
	returnResults = []
	for i in rawResults:
		returnResults.append(i[2].partition(' playing ')[0])

	return returnResults

def insertAndReturnRecentSong():
	#checkForTwitterFDW()
	cursor = connection.cursor()
	cursor.execute('SELECT from_user, created_at, text \
	FROM twitter \
	WHERE q=%s and from_user=%s \
	order by created_at Desc limit 1',
	['bpm_playlist','bpm_playlist'])
	live_row = cursor.fetchone()

	a = TweetInfo.objects.latest('created_at')
	
	#checks whether there's a newer tweet 
	if (live_row[1] > a.created_at):
		insert = TweetInfo(from_user=live_row[0], created_at=live_row[1], text=live_row[2])
		insert.save()

	a = TweetInfo.objects.latest('created_at')
	#splits the tweet 
	#this is assuming that every tweet has been following the same format ('author - songname playing on #BPM')
	#could easily break assuming the tweet format has changed
	partition = a.text.partition(' playing ')
	return partition[0]