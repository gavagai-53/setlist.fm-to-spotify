#! /usr/bin/python
#! coding: utf-8

"""
    SETLIST.FM TO SPOTIFY -- Setlist.fm caller
    
    This code makes a call to the Setlist.fm API to retrieve a setlist.
"""

import cgi, cgitb
import requests
import json
import datetime

arguments = cgi.FieldStorage()

artist = arguments.getvalue('artist')
city = arguments.getvalue('city')
year = arguments.getvalue('year')
concert_id = arguments.getvalue('id')

setlistfm-api-key = "" # Insert your setlist.fm API key here

headers = {	'x-api-key': setlistfm-api-key,
			'Accept' : 'application/json'}

def get_setlist(concert):
	artist = concert['artist']['name']
	date = datetime.datetime.strptime(concert['eventDate'], '%d-%m-%Y').strftime('%b %d, %Y')

	setlist = concert['sets']['set']

	songs = []
	for set_part in setlist:
		for song in set_part['song']:
			songs.append(song['name'])

	reply = {	'id':concert['id'],
				'songs':songs,
				'venue':False	}

	print json.dumps(reply)

print "Content-type:application/json\r\n\r\n"

if not concert_id:
	params = {	'artistName':artist,
				'cityName':city,
				'year':year }

	response = requests.get('https://api.setlist.fm/rest/1.0/search/setlists', headers=headers, params=params)

	total = json.loads(response._content)['total']

	if total > 1:
		
		concerts = json.loads(response._content)['setlist']
		venues = []

		for concert in concerts:
			date = ' (' + datetime.datetime.strptime(concert['eventDate'], '%d-%m-%Y').strftime('%b %d, %Y') + ')'
			venue = [concert['id'], concert['venue']['name'] + date]
			venues.append(venue)

		reply = { 'venue': True,
					'venues':venues}

		print json.dumps(reply)


	else:
		concert = json.loads(response._content)['setlist'][0]
		get_setlist(concert)

else:
	response = requests.get('https://api.setlist.fm/rest/1.0/setlist/' + concert_id, headers=headers)
	concert = json.loads(response._content)
	get_setlist(concert)

