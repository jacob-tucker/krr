import h5py
import tables
# Filenames + Dir
dir = "./sample/"
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
print(f"The number of songs in this file is: {h5file.root.metadata.songs.nrows}")
print(f"The artist name is: {h5file.root.metadata.songs.cols.artist_name[0]}")
print(f"The song title is: {h5file.root.metadata.songs.cols.title[0]}")
print(f"The song's danceability is: {h5file.root.analysis.songs.cols.danceability[0]}")
print(f"The song's energy is: {h5file.root.analysis.songs.cols.energy[0]}")
print(f"The song's loudness is: {h5file.root.analysis.songs.cols.loudness[0]}")
print("\n")
print(f"The number of songs in this file is: {h5file_2.root.metadata.songs.nrows}")
print(f"The artist name is: {h5file_2.root.metadata.songs.cols.artist_name[0]}")
print(f"The song title is: {h5file_2.root.metadata.songs.cols.title[0]}")
print(f"The song's danceability is: {h5file_2.root.analysis.songs.cols.danceability[0]}")
print(f"The song's energy is: {h5file_2.root.analysis.songs.cols.energy[0]}")
print(f"The song's loudness is: {h5file_2.root.analysis.songs.cols.loudness[0]}")
print("\n")
print(f"The number of songs in this file is: {h5file_3.root.metadata.songs.nrows}")
song_info_dict = {}
song_titles = []
num_songs = h5file_3.root.metadata.songs.nrows
for song_idx in range(20):
  # Get Data
  song_title = h5file_3.root.metadata.songs.cols.title[song_idx].decode()
  song_artist = h5file_3.root.metadata.songs.cols.artist_name[song_idx].decode()
  song_danceability = h5file_3.root.analysis.songs.cols.danceability[song_idx] 
  song_energy = h5file_3.root.analysis.songs.cols.energy[song_idx]
  song_loudness = h5file_3.root.analysis.songs.cols.loudness[song_idx]
  # Add to song_info_dict
  song_info_dict[song_title] = []
  song_info_dict[song_title].append(song_artist)
  song_info_dict[song_title].append(song_danceability)
  song_info_dict[song_title].append(song_energy)
  song_info_dict[song_title].append(song_loudness)
  song_titles.append(song_title)

count = 0
print(song_info_dict)
for song_title in song_titles:
  if count == 20:
    break
  print(f"The song title is: {song_title}")
  print(f"The song artist is: {song_info_dict[song_title][0]}")
  print(f"The song danceability is: {song_info_dict[song_title][1]}")
  print(f"The song energy is: {song_info_dict[song_title][2]}")
  print(f"The song loudness is: {song_info_dict[song_title][3]}\n\n")
  count += 1