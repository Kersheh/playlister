import sys, json, random
import spotipy
import spotipy.util as util
import youtubeSearch

#todo: create class to avoid global vars
sp = {}
username = ''

# Script setup

def config():
    with open('config.json') as data:
        config = json.load(data)
    return config['config']

def get_token(params):
    return util.prompt_for_user_token(username=params['username'],
                                      client_id=params['id'], \
                                      client_secret=params['secret'], \
                                      redirect_uri=params['redirect_uri'], \
                                      scope='user-library-read')

def init_sp():
    global username
    global sp

    params = config()
    username = params['username']
    token = get_token(params)
    if not token:
        print("Can't get token for", username)
        sys.exit()
    else:
        sp = spotipy.Spotify(auth=token)

# Playlist interactions

def get_all_playlists():
    return sp.user_playlists(username)

def print_playlist_names():
    playlists = get_all_playlists()
    for playlist in playlists['items']:
        print playlist['name']

def get_playlist_id(pl):
    playlists = get_all_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == pl:
            return playlist['id']
    print "Playlist {} not found".format(pl)
    return ''

def get_playlist_tracks(pl_id):
    try:
        tracks = []
        results = sp.user_playlist_tracks(username, playlist_id=pl_id)
        for track in results['items']:
            tracks.append((track['track']['name'] + ' - ' + track['track']['artists'][0]['name']).encode('utf-8'))
        return tracks
    except:
        print 'Invalid playlist id'
        return []


def export_youtube_playlist(tracks, output='autoplaylist.txt', shuffle=False):
    if shuffle:
        random.shuffle(tracks)
    print 'Exporting playlist to {}'.format(output)
    with open(output, 'w') as file_out:
        for track in tracks:
            youtube_url = youtubeSearch.query_video_url(track)
            print track, youtube_url
            file_out.write(youtube_url + '\n')
    print 'Export complete.'

if __name__ == '__main__':
    playlist = 'Summer \'17'
    init_sp()

    pl_id = get_playlist_id(playlist)
    tracks = get_playlist_tracks(pl_id)
    export_youtube_playlist(tracks, shuffle=True)
