import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import re
cid = 'a461fd950e6a4a36ae8c0cd1172d9021'
secret = '706116abeaba42e6872ebc2678268b27'
auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

if len(sys.argv) > 1:
    print(' '.join(sys.argv[1:]))
    name = ' '.join(sys.argv[1:])
else:
    name = 'Take me Home'

track_info = spotify.search(q='track: ' + name)
track_name = re.sub('[^0-9a-zA-Z]+', "", track_info['tracks']['items'][0]['name'])
track_popularity = track_info['tracks']['items'][0]['popularity']
track_id = track_info['tracks']['items'][0]['id']
print(track_name)
print(track_popularity)

results = spotify.audio_features(track_id)
analysis = results[0]
print(analysis)


