import sys
import praw
import json
import requests

def get_songlist_reddit(keys):
    reddit = praw.Reddit(client_id = keys[0],
                 client_secret = keys[1],
                     user_agent = keys[2])

    songs_added = 0
    song = ''
    #add 10 songs to the playlist
    for submission in reddit.subreddit('listentothis').new(limit=None):
	    song = submission.title.split('[')[0]
	    print song
	    if search_song(keys, song):
		songs_added = songs_added + 1
		if songs_added >= 10:
			break


def search_song(keys, song):
   #searching for songs to add to playlist
   params = {
	'client_id': keys[3],
	'response_type': 'code',
	'redirect_uri': 'https://example.com/callback/',
	'scope': 'playlist-modify-public playlist-modify-private'
   }

   url = 'https://accounts.spotify.com/authorize'

   s = requests.get('https://accounts.spotify.com/authorize', params = params)

   #auth code
   s = keys[4]

   headers = {
       'Accept': 'application/json',
       'Authorization': 'Bearer ' + s
   }

   params = {
 	   'q': song,
           'type': 'track'
   }

   r = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)

   json_data = json.loads(r.text)
   #parse for song info -- if song found return True, else return False
   try:
   	uid = json_data['tracks']['items'][0]['uri']
   except:
	return False
   add_to_playlist(keys, s, uid)
   return True

def add_to_playlist(keys, s, uid):

   headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + s,
   }

   params = {
	'uris': uid
   }
   #add to playlist
   requests.post('https://api.spotify.com/v1/users/' + keys[5] + '/playlists/' + keys[6] + '/tracks', params = params, headers=headers)

if __name__ == "__main__":
    #maintain a list for private keys
    keys = []
    try:
	with open("keys.txt", "r") as f:
		keys = [line.strip() for line in f]
    except:
	print "There was a problem with the input file. Aborting..."
	sys.exit(0)
    get_songlist_reddit(keys)
