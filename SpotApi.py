#!/usr/bin/env python3
# -*- coding: utf-8 -*-







client_id = 'a643c85d4695476d9000ffd3a75cf67d'
client_secret = 'ed9aafa6e9c446bb8325971f0e1c0228'


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])