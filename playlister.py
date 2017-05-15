import sys, json

import spotipy
import spotipy.util as util

with open('config.json') as data:
    config = json.load(data)

params = config['config']
username = params['username']

token = util.prompt_for_user_token(username=username, client_id=params['id'], \
                                   client_secret=params['secret'], redirect_uri=params['redirect_uri'], \
                                   scope='user-library-read')

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        print(playlist['name'])
else:
    print("Can't get token for", username)
