import h5py
import tables
import re

### POPULATING INITIAL KRF FILE ###
f = open("demo_krf_file.krf", "w")

f.write('''
;; An example of what should autopopulate the file

(in-microtheory SongsMt)
(isa SongsMt Microtheory)
(comment SongsMt
  "SongsMt is a microtheory about songs and how they relate to one another. It includes HORN clauses inFIRE.")
(genlMt SongsMt KioskDataMt) ;; Uses knowledge from the CS Kiosk

(isa MillionSong Collection)
(genls MillionSong MusicalComposition)
(comment MillionSong
 "A song is a MillionSong if it is from the Million Songs Dataset.")

;;; Predicates

(isa fastSong Predicate)
(arity fastSong 1)
(arg1Isa fastSong MillionSong)
(comment fastSong
 "(fastSong ?millionsong) indicates that ?millionsong has a tempo above 120.0.")

(isa slowSong Predicate)
(arity slowSong 1)
(arg1Isa slowSong MillionSong)
(comment slowSong
 "(slowSong ?millionsong) indicates that ?millionsong has a tempo below 120.0.")

(isa loudSong Predicate)
(arity loudSong 1)
(arg1Isa loudSong MillionSong)
(comment loudSong
 "(loudSong ?millionsong) indicates that ?millionsong has a loudness above -10.0.")

(isa quietSong Predicate)
(arity quietSong 1)
(arg1Isa quietSong MillionSong)
(comment quietSong
 "(quietSong ?millionsong) indicates that ?millionsong has a loudness below -10.0.")

(isa longSong Predicate)
(arity longSong 1)
(arg1Isa longSong MillionSong)
(comment longSong
 "(longSong ?millionsong) indicates that ?millionsong has a duration above 240.")
 
''')
###################################

# Filenames + Dir
dir = "/content/drive/MyDrive/371_Data/"
filename_1 = "TRAAAMQ128F1460CD3.h5"
filename_2 = "TRAAAAW128F429D538.h5"
filename_3 = "msd_summary_file.h5"
file_path_1 = dir + filename_1
file_path_2 = dir + filename_2
file_path_3 = dir + filename_3
# H5PY Open
dataset = h5py.File(file_path_1, "r")
# PyTables Open
h5file = tables.open_file(file_path_1, mode='r')
h5file_2 = tables.open_file(file_path_2, mode='r')
h5file_3 = tables.open_file(file_path_3, mode='r')
# Use Pytables
# print(f"The number of songs in this file is: {h5file.root.metadata.songs.nrows}")
# print(f"The artist name is: {h5file.root.metadata.songs.cols.artist_name[0]}")
# print(f"The song title is: {h5file.root.metadata.songs.cols.title[0]}")
# print(f"The song's danceability is: {h5file.root.analysis.songs.cols.danceability[0]}")
# print(f"The song's energy is: {h5file.root.analysis.songs.cols.energy[0]}")
# print(f"The song's loudness is: {h5file.root.analysis.songs.cols.loudness[0]}")
# print(f"The song's duration is: {h5file.root.analysis.songs.cols.duration[0]}")
# print(f"The song's tempo is: {h5file.root.analysis.songs.cols.tempo[0]}")
# print("\n")
# print(f"The number of songs in this file is: {h5file_2.root.metadata.songs.nrows}")
# print(f"The artist name is: {h5file_2.root.metadata.songs.cols.artist_name[0]}")
# print(f"The song title is: {h5file_2.root.metadata.songs.cols.title[0]}")
# print(f"The song's danceability is: {h5file_2.root.analysis.songs.cols.danceability[0]}")
# print(f"The song's energy is: {h5file_2.root.analysis.songs.cols.energy[0]}")
# print(f"The song's loudness is: {h5file_2.root.analysis.songs.cols.loudness[0]}")
# print(f"The song's duration is: {h5file_2.root.analysis.songs.cols.duration[0]}")
# print(f"The song's tempo is: {h5file_2.root.analysis.songs.cols.tempo[0]}")
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
  f.write("(isa {} MillionSong)\n".format(song_title))
  
  
f.write("\n;;; Tempo classifications\n\n")
for song_title in song_titles:
  song_tempo = song_info_dict[song_title][5]
  if song_tempo >= 120.0:
    f.write("(fastSong {})\n".format(song_title))
  else:
    f.write("(slowSong {})\n".format(song_title))

f.write("\n;;; Loudness classifications\n\n")
for song_title in song_titles:
  song_loudness = song_info_dict[song_title][3]
  if song_loudness >= -10.0:
    f.write("(loudSong {})\n".format(song_title))
  else:
    f.write("(quietSong {})\n".format(song_title))

f.write("\n;;; Duration classifications\n\n")
for song_title in song_titles:
  song_duration = song_info_dict[song_title][4]
  if song_duration >= 240:
    f.write("(longSong {})\n".format(song_title))

f.write('''\n\n
(isa goodRockSong Predicate)
(arity goodRockSong 1)
(arg1Isa goodRockSong MillionSong)
(comment goodRockSong
 "(goodRockSong ?millionsong) indicates that ?millionsong is a loudSong and not a quietSong.")

(<== (goodRockSong ?millionsong)
     (loudSong ?millionsong)
     (fastSong ?millionsong)
     (uninferredSentence (quietSong ?millionsong))) ;; Skip if ?millionsong is loud

(<== (isa ?song weddingSong)
     (quietSong ?song)
     (longSong ?song))

(<== (isa ?song elevatorSong)
     (quietSong ?song)
     (slowSong ?song)
     (longSong ?song))

(<== (isa ?song coffeeShopSong)
     (slowSong ?song)
     (quietSong ?song))
''')
f.close()