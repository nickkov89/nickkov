www.nickkov.com
=======

Built with Django, running on Nginx+Gunicorn 


TweetPlay (www.nickkov.com/tweetplay)
=======
Built on top of Postgres

Postgres polls Twitter channel @bpm_playlist and gets the most recently tweeted song
Song is parsed by Python and spit out into the template
YouTube API is used to search for the top 3 hits, and the first one plays automatically
When song is finished, player state changes and JS refreshes the page
Postgres polls the Twitter channel and if there is a new tweet the process is started over.

Issues:
This tool is mainly dependant on the Twitter channel. Fortunately, @bpm_playlist follows an
identical pattern to every Tweet thus making the parsing very easy.
Unfortunately, if there is ever a typo, or if the current song playing is over before there is a 
new tweet, the app breaks and a page refresh is needed to repoll.

Solutions:
If there is a typo and YouTube-API gives back 0 search results, simply display an error message to 
the user, and then refresh the page in 5 minutes automatically.
If the song currently tweeted is not updated before the song is done playing, store songs in Postgres
and compare last added song to newly polled song, if they're the same, either display an error message
and refresh the page every 20 seconds until there is a new tweet, or prompt user with whether they want
to just play the same song one more time.

I don't really care to add these features since this app was built mainly to show how cool Postgres' 
foreign data wrapper function is. Perhaps in the future when I have more time, I'll add a history and present
a proper fix for the potential problems.  

DormRoof
=======

A work in progress. An RA administration/Student dorm network tool. 

Models are more or less all set up, the frontend is completely missing since I am not a huge fan of it.

Also, migrated into it's own repo (dormpad) recently in order to convert to better Django practices.
