# coding=utf-8

import dbus
from collections import OrderedDict

import spotipy

from rotify.rofi import rofi


spotify = spotipy.Spotify()


def open_uri(*uris):
    session = dbus.SessionBus()
    player = session.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    interface = dbus.Interface(player, dbus_interface='org.mpris.MediaPlayer2.Player')

    interface.Pause()
    for uri in uris:
        interface.OpenUri(uri)


def items_to_dict(items):
    return OrderedDict([(item['name'], item['uri']) for item in items])


def _search(query, type_):
    results = spotify.search(q=query, type=type_)
    from pprint import pprint
    pprint(results)
    items = items_to_dict(results['%ss' % type_]['items'])

    return items


def search_songs():
    tracks = _search(rofi(), 'track')
    track_uri = tracks[rofi(tracks.keys())]

    open_uri(track_uri)


def search_albums():
    albums = _search(rofi(), 'album')
    album_uri = albums[rofi(albums.keys())]

    results = spotify.album_tracks(album_uri)
    print results
    tracks = items_to_dict(results['items'])
    track_uri = tracks[rofi(tracks.keys())]

    open_uri(album_uri, track_uri)


def search_artists():
    artists = _search(rofi(), 'artist')
    artist_uri = artists[rofi(artists.keys())]

    results = spotify.artist_albums(artist_uri)
    albums = items_to_dict(results['items'])
    options = ['Top Tracks'] + albums.keys()
    album_uri = albums[rofi(options)]

    results = spotify.album_tracks(album_uri)
    tracks = items_to_dict(results['items'])
    track_uri = tracks[rofi(tracks.keys())]

    open_uri(artist_uri, track_uri)


def search_playlists():
    # XXX Not working
    playlists = _search(rofi(), 'playlist')
    full_uri = playlists[rofi(playlists.keys())]
    full_uri = full_uri.split(':')
    user_uri = full_uri[2]
    playlist_uri = ':'.join(full_uri[:1] + full_uri[3:])

    results = spotify.user_playlist_tracks(user_uri, playlist_uri)
    tracks = items_to_dict(results['items'])
    track_uri = tracks[rofi(tracks.keys())]

    open_uri(playlist_uri, track_uri)
