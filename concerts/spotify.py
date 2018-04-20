#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi, cgitb
import requests
import json
import datetime
import spotipy
import spotipy.util as util
import sys

print "Content-type:application/json\n\n"

#Pass console output to a file temporarily. It won't be returned to the browser until the end.
old = sys.stdout
sys.stdout = open('file.txt', 'w')
sys.stderr = sys.stdout

reply = {}

arguments = cgi.FieldStorage()
concert_id = arguments.getvalue('id')

songs = []
spotify_list = []

#Spotify Variables
client_id=''
client_secret = ''
redirect_uri = ''
code = arguments.getvalue('code')
refresh = arguments.getvalue('refresh')

#Setlist.fm API key
setlistfm-api-key = ''

headers = {	'x-api-key': setlistfm-api-key,
			'Accept' : 'application/json'}

response = requests.get('https://api.setlist.fm/rest/1.0/setlist/' + concert_id, headers=headers)
concert = json.loads(response._content)

venue = concert['venue']['name']
artist = concert['artist']['name']
city = concert['venue']['city']['name'] + ', ' + concert['venue']['city']['country']['name']
date = datetime.datetime.strptime(concert['eventDate'], '%d-%m-%Y').strftime('%b %d, %Y')

name = artist + ' at ' + venue + ' (' + city + ') ' + ' - ' + date

setlist = concert['sets']['set']

for set_part in setlist:
	for song in set_part['song']:
		songs.append(song['name'])

def get_token(code, refresh=False): #Use web code, set refresh to true if we have a refresh code

	# Prepare a post request with the code
	if not refresh:
		grant_type = 'authorization_code'
		payload = {'code':code, 'grant_type':grant_type, 'redirect_uri':redirect_uri, 'client_id':client_id, 'client_secret':client_secret}
	else:
		grant_type = 'refresh_token'
		payload = {'refresh_token':code, 'grant_type':grant_type, 'redirect_uri':redirect_uri, 'client_id':client_id, 'client_secret':client_secret}

	# Make the POST request
	server_response = requests.post('https://accounts.spotify.com/api/token', data=payload)

	#Get the refresh token for future use
	try:
		refresh = json.loads(server_response.text)['refresh_token']
		reply['refresh'] = refresh
	except:
		pass

	#Get the access token for API call and return it
	token = json.loads(server_response.text)['access_token']
	return token

def spotify(songs, token):

	#Start calling API
	sp = spotipy.Spotify(auth = token)

	#Clear the lists
	spotify_list = []

	#For every row, get song title
	for song in songs:
		# To do: find a way to get albums

		#Add title and album and search on Spotify
		search_str = 'title:' + song +  ' ' + 'artist:' + artist
		search_str = search_str.encode('utf-8', 'ignore')

		#Check whether we get data from Spotify API first
		if sp.search(q=search_str, limit=1, type='track')['tracks']['items']:
			song_uri = sp.search(q=search_str, limit=1, type='track')['tracks']['items'][0]['uri']
			#Avoid duplicates
			if song_uri not in spotify_list:
				spotify_list.append(song_uri) #Add URI to the list

	#Create the playlist and add the songs
	user = sp.me()['id']
	reply['success'] = True
	playlist = sp.user_playlist_create(user, name, public=False)
	playlist_id = playlist['id']
	adding = sp.user_playlist_add_tracks(user, playlist_id, spotify_list)
	reply['url'] = playlist['uri']

if not refresh:
	reply['code'] = True
	token = get_token(code)
else:
	reply['code'] = False
	token = get_token(refresh, True)

spotify(songs,token)
sys.stdout = old
print json.dumps(reply)
