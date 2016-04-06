# coding=utf-8

# import dbus
from rotify.rofi import rofi
from rotify import search
# from collections import OrderedDict


def search_rofi():
    selected = rofi([
        'Songs',
        'Albums',
        'Artists',
        'Playlists',
        '--------------',
        'Exit'
    ])

    if selected == 'Songs':
        search.search_songs()
    elif selected == 'Albums':
        search.search_albums()
    elif selected == 'Artists':
        search.search_artists()
    elif selected == 'Playlists':
        rofi(['Not implemented yet!'])
    else:
        return 0


def main():
    selected = rofi([
        'Search',
        '--------------',
        'Songs',
        'Albums',
        'Artists',
        'Playlists',
        '--------------',
        'Exit'
    ])

    if selected == 'Search':
        search_rofi()
    elif selected == 'Songs':
        rofi(['Not implemented yet!'])
    elif selected == 'Albums':
        rofi(['Not implemented yet!'])
    elif selected == 'Artists':
        rofi(['Not implemented yet!'])
    elif selected == 'Playlists':
        rofi(['Not implemented yet!'])
    else:
        return 0
