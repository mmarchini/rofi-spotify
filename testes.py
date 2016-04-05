#coding=utf-8

import dbus
from subprocess import Popen, PIPE
from collections import OrderedDict

import spotipy

spotify = spotipy.Spotify()

# Search for artist
p = Popen(['rofi', '-dmenu', '-p', 'Search Artist:'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
selected, _ = p.communicate()

#
results = spotify.search(q=selected, type='artist')
artists = OrderedDict([(a['name'], a['uri']) for a in results['artists']['items']])
p = Popen(['rofi', '-dmenu', '-p', 'Select:'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
selected, _ = p.communicate('\n'.join([a.encode('utf-8') for a in artists.keys()]))
artist_uri = artists[selected.strip()]

results = spotify.artist_albums(artist_uri)
albums = OrderedDict([(a['name'], a['uri']) for a in results['items']])
p = Popen(['rofi', '-dmenu', '-p', 'Album:'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
selected, _ = p.communicate('\n'.join([a.encode('utf-8') for a in albums.keys()]))
album_uri = albums[selected.strip()]

tracks = spotify.album_tracks(album_uri)
first_track = tracks['items'][0]['uri']
print album_uri, first_track

session = dbus.SessionBus()
player= session.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
interface = dbus.Interface(player, dbus_interface='org.mpris.MediaPlayer2.Player')

interface.Pause()
interface.OpenUri(album_uri)
interface.OpenUri(first_track)
