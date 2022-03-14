import h5py
import tables
import re

### SPOTIPY
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
custom_track_popularity = track_info['tracks']['items'][0]['popularity']
custom_track_id = track_info['tracks']['items'][0]['id']

results = spotify.audio_features(custom_track_id)
custom_analysis = results[0]
print(custom_analysis)
###

### POPULATING INITIAL KRF FILE ###
f = open("demo_krf_file.krf", "w")

f.write('''
;; An example of what should autopopulate the file

(in-microtheory SongsMt)
(isa SongsMt Microtheory)
(comment SongsMt
  "SongsMt is a microtheory about songs and how they relate to one another. It includes HORN clauses inFIRE.")
(genlMt SongsMt KioskDataMt) ;; Uses knowledge from the CS Kiosk

(isa WeddingMusicalCompositionTypeByGenre Collection)
(genls WeddingMusicalCompositionTypeByGenre MusicalCompositionTypeByGenre)
(comment WeddingMusicalCompositionTypeByGenre
 "This is a collection of songs that could be played at weddings.")

(isa ElevatorMusicalCompositionTypeByGenre Collection)
(genls ElevatorMusicalCompositionTypeByGenre MusicalCompositionTypeByGenre)
(comment ElevatorMusicalCompositionTypeByGenre
 "This is a collection of songs that could be played inside of an elevator.")

(isa CoffeeShopMusicalCompositionTypeByGenre Collection)
(genls CoffeeShopMusicalCompositionTypeByGenre MusicalCompositionTypeByGenre)
(comment CoffeeShopMusicalCompositionTypeByGenre
 "This is a collection of songs that could be played at a coffee shop.")

(isa PopMusicalCompositionTypeByGenre Collection)
(genls PopMusicalCompositionTypeByGenre MusicalCompositionTypeByGenre)
(comment PopMusicalCompositionTypeByGenre
 "This is a collection of songs that fit in the pop category.")

;;; Predicates

(isa fastSong Predicate)
(arity fastSong 1)
(arg1Isa fastSong MusicalComposition)
(comment fastSong
 "(fastSong ?song) indicates that ?song has a tempo above 120.0.")

(isa slowSong Predicate)
(arity slowSong 1)
(arg1Isa slowSong MusicalComposition)
(comment slowSong
 "(slowSong ?song) indicates that ?song has a tempo below 120.0.")

(isa loudSong Predicate)
(arity loudSong 1)
(arg1Isa loudSong MusicalComposition)
(comment loudSong
 "(loudSong ?song) indicates that ?song has a loudness above -10.0.")

(isa quietSong Predicate)
(arity quietSong 1)
(arg1Isa quietSong MusicalComposition)
(comment quietSong
 "(quietSong ?song) indicates that ?song has a loudness below -10.0.")

(isa longSong Predicate)
(arity longSong 1)
(arg1Isa longSong MusicalComposition)
(comment longSong
 "(longSong ?song) indicates that ?song has a duration above 240.")

(isa danceableSong Predicate)
(arity danceableSong 1)
(arg1Isa danceableSong MusicalComposition)
(comment danceableSong
 "(danceableSong ?song) indicates that ?song is danceable.")

(isa energeticSong Predicate)
(arity energeticSong 1)
(arg1Isa energeticSong MusicalComposition)
(comment energeticSong
 "(energeticSong ?song) indicates that ?song is an energetic song.")

(isa popularSong Predicate)
(arity popularSong 1)
(arg1Isa popularSong MusicalComposition)
(comment popularSong
 "(popularSong ?song) indicates that ?song is popular.")

(isa acousticSong Predicate)
(arity acousticSong 1)
(arg1Isa acousticSong MusicalComposition)
(comment acousticSong
 "(popularSong ?song) indicates that ?song is an acoustic song.")
 
''')
###################################

# Filenames + Dir
dir = ""
filename_3 = "msd_summary_file.h5"
file_path_3 = dir + filename_3
# PyTables Open
h5file_3 = tables.open_file(file_path_3, mode='r')

print("\n")
print(f"The number of songs in this file is: {h5file_3.root.metadata.songs.nrows}")
song_info_dict = {}
song_titles = []
num_songs = h5file_3.root.metadata.songs.nrows

### Our Ids ###
ourIds = []
for id in ourIds:
  # Get Data
  song_title = h5file_3.root.metadata.songs.cols.title[id].decode()
  song_artist = h5file_3.root.metadata.songs.cols.artist_name[id].decode()
  song_danceability = h5file_3.root.analysis.songs.cols.danceability[id] 
  song_energy = h5file_3.root.analysis.songs.cols.energy[id]
  song_loudness = h5file_3.root.analysis.songs.cols.loudness[id]
  song_duration = h5file_3.root.analysis.songs.cols.duration[id]
  song_tempo = h5file_3.root.analysis.songs.cols.tempo[id]
  # Add to song_info_dict
  song_info_dict[song_title] = []
  song_info_dict[song_title].append(song_artist)
  song_info_dict[song_title].append(song_danceability)
  song_info_dict[song_title].append(song_energy)
  song_info_dict[song_title].append(song_loudness)
  song_info_dict[song_title].append(song_duration)
  song_info_dict[song_title].append(song_tempo)
  song_titles.append(song_title)
###############

for song_idx in range(50):
  # Get Data
  song_title = h5file_3.root.metadata.songs.cols.title[song_idx].decode()
  song_title = re.sub('[^0-9a-zA-Z]+', "", song_title)
  song_artist = h5file_3.root.metadata.songs.cols.artist_name[song_idx].decode()
  song_danceability = h5file_3.root.analysis.songs.cols.danceability[song_idx] 
  song_energy = h5file_3.root.analysis.songs.cols.energy[song_idx]
  song_loudness = h5file_3.root.analysis.songs.cols.loudness[song_idx]
  song_duration = h5file_3.root.analysis.songs.cols.duration[song_idx]
  song_tempo = h5file_3.root.analysis.songs.cols.tempo[song_idx]
  # Add to song_info_dict
  song_info_dict[song_title] = []
  song_info_dict[song_title].append(song_artist)
  song_info_dict[song_title].append(song_danceability)
  song_info_dict[song_title].append(song_energy)
  song_info_dict[song_title].append(song_loudness)
  song_info_dict[song_title].append(song_duration)
  song_info_dict[song_title].append(song_tempo)
  song_titles.append(song_title)

count = 0
for song_title in song_titles:
  print(f"The song title is: {song_title}")
  print(f"The song artist is: {song_info_dict[song_title][0]}")
  print(f"The song danceability is: {song_info_dict[song_title][1]}")
  print(f"The song energy is: {song_info_dict[song_title][2]}")
  print(f"The song loudness is: {song_info_dict[song_title][3]}")
  print(f"The song duration is: {song_info_dict[song_title][4]}")
  print(f"The song tempo is: {song_info_dict[song_title][5]}\n\n")
  count += 1

### ADDING INFO TO KRF FILE ###
f.write(";;; Songs\n\n")
for song_title in song_titles:
  f.write("(isa {} MusicalComposition)\n".format(song_title))
f.write("(isa {} MusicalComposition)\n".format(track_name))
  
f.write("\n;;; Tempo classifications\n\n")
for song_title in song_titles:
  song_tempo = song_info_dict[song_title][5]
  if song_tempo >= 120.0:
    f.write("(fastSong {})\n".format(song_title))
  else:
    f.write("(slowSong {})\n".format(song_title))
if custom_analysis['tempo'] >= 120.0:
  f.write("(fastSong {})\n".format(track_name))
else:
    f.write("(slowSong {})\n".format(track_name))

f.write("\n;;; Loudness classifications\n\n")
for song_title in song_titles:
  song_loudness = song_info_dict[song_title][3]
  if song_loudness >= -10.0:
    f.write("(loudSong {})\n".format(song_title))
  else:
    f.write("(quietSong {})\n".format(song_title))
if custom_analysis['loudness'] >= -10.0:
  f.write("(loudSong {})\n".format(track_name))
else:
    f.write("(quietSong {})\n".format(track_name))

f.write("\n;;; Duration classifications\n\n")
for song_title in song_titles:
  song_duration = song_info_dict[song_title][4]
  if song_duration >= 240:
    f.write("(longSong {})\n".format(song_title))
if (custom_analysis['duration_ms']/1000) >= 240:
  f.write("(longSong {})\n".format(track_name))

f.write("\n;;; Danceability classifications\n\n")
if custom_analysis['danceability'] >= .6:
  f.write("(danceableSong {})\n".format(track_name))

f.write("\n;;; Energy classifications\n\n")
if custom_analysis['energy'] >= .75:
  f.write("(energeticSong {})\n".format(track_name))

f.write("\n;;; Popularity classifications\n\n")
if custom_track_popularity >= 50:
  f.write("(popularSong {})\n".format(track_name))

f.write("\n;;; Acousticness classifications\n\n")
print(custom_analysis['acousticness'])
if custom_analysis['acousticness'] >= .75:
  f.write("(acousticSong {})\n".format(track_name))

f.write('''\n\n
(isa popularRockSong Predicate)
(arity popularRockSong 1)
(arg1Isa popularRockSong MusicalComposition)
(comment popularRockSong
 "(popularRockSong ?song) indicates that ?song is both popular and a rock song.")

(isa goodRockSong Predicate)
(arity goodRockSong 1)
(arg1Isa goodRockSong MusicalComposition)
(comment goodRockSong
 "(goodRockSong ?song) indicates that ?song is a MusicalComposition and not a rock song.")

(isa popularPopSong Predicate)
(arity popularPopSong 1)
(arg1Isa popularPopSong MusicalComposition)
(comment popularPopSong
 "(popularPopSong ?song) indicates that ?song is a popular and a pop song.")

(isa aloneTimeSong Predicate)
(arity aloneTimeSong 1)
(arg1Isa aloneTimeSong MusicalComposition)
(comment aloneTimeSong
 "(aloneTimeSong ?song) indicates that ?song is a song you listen to when you are alone and want to focus on yourself.")

(isa fitnessSong Predicate)
(arity fitnessSong 1)
(arg1Isa fitnessSong MusicalComposition)
(comment fitnessSong
 "(fitnessSong ?song) indicates that ?song is a song you listen to when you are doing fitness.")

(<== (fitnessSong ?song)
     (fastSong ?song)
     (energeticSong ?song) 
     (danceableSong ?song))

(<== (popularRockSong ?song)
     (popularSong ?song)
     (isa ?song RockMusicalCompositionTypeByGenre))

(<== (popularPopSong ?song)
     (popularSong ?song)
     (isa ?song PopMusicalCompositionTypeByGenre))

(<== (goodRockSong ?song)
     (isa ?song MusicalComposition)
     (isa ?song RockMusicalCompositionTypeByGenre))

(<== (aloneTimeSong ?song)
     (quietSong ?song)
     (slowSong ?song))

(<== (isa ?song WeddingMusicalCompositionTypeByGenre)
     (quietSong ?song)
     (longSong ?song))

(<== (isa ?song ElevatorMusicalCompositionTypeByGenre)
     (quietSong ?song)
     (slowSong ?song)
     (longSong ?song))

(<== (isa ?song CoffeeShopMusicalCompositionTypeByGenre)
     (slowSong ?song)
     (quietSong ?song))

(<== (isa ?song RockMusicalCompositionTypeByGenre)
     (loudSong ?song)
     (uninferredSentence (quietSong ?song)))

(<== (isa ?song PopMusicalCompositionTypeByGenre)
     (loudSong ?song)
     (fastSong ?song)
     (danceableSong ?song))
''')
f.close()