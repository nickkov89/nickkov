from django.db import models
from django.db import connections
from django.db import DatabaseError
import HTMLParser

class TweetInfo(models.Model):
	from_user = models.CharField(max_length=20)
	created_at = models.DateTimeField()
	text = models.TextField()

	def __unicode__(self):
		return "from: " + self.from_user + ":    " + self.text

#max is 15 based on Twitter's API
def getLatestSongs(num):
	cursor = connections['postgres'].cursor()
	cursor.execute('SELECT text \
	FROM twitter \
	WHERE q=%s and from_user=%s \
	ORDER BY created_at DESC LIMIT '+str(num),
	['bpm_playlist','bpm_playlist'])

	rows = cursor.fetchall()
	partitioned_list = []
	for row in rows:
		partitioned_list.append(HTMLParser.HTMLParser().unescape(row[0].partition(' playing ')[0]))

	return partitioned_list

def insertAndReturnRecentSong():
	cursor = connections['postgres'].cursor()
	cursor.execute('SELECT from_user, created_at, text \
	FROM twitter \
	WHERE q=%s and from_user=%s \
	ORDER BY created_at DESC LIMIT 1',
	['bpm_playlist','bpm_playlist'])
	live_row = cursor.fetchone()

	latest_local = TweetInfo.objects.using('postgres').latest('created_at')
	
	#checks whether there's a newer tweet 
	if (live_row[1] > latest_local.created_at):
		insert = TweetInfo(from_user=live_row[0], created_at=live_row[1], text=live_row[2])
		insert.save(using='postgres')

	#splits the tweet 
	#this is assuming that every tweet has been following the same format ('author - songname playing on #BPM')
	#could break assuming the tweet format has changed
	partition = latest_local.text.partition(' playing ')
	return partition[0]
