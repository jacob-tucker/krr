# Musical QA

Welcome to our project! This folder contains all of the code we used for our demonstrations and reasonings. I will explain each file:

## create_file.py

This is where most of our work went in. This python script generated a .krf file with all of our predicates, Collections, entities, and Horn clauses. This file does many things:

- Pulls songs from both the Million Song Database (using the `msd_summary_file.h5`) AND the Spotify API. The user can input a song into the command line when running the script, for example: `python3 create_file.py Barbie Girl` in order to include the song "Barbie Girl" in our reasonings.
- Loops through a ton of songs from the MSD and assigns them basic predicates like "loudSong" and "slowSong".
- Develops more complex predicates for the song retrieved from Spotify API, like "danceableSong" and "energeticSong"
- Sets thresholds for songs to meet the requirements to assume those predicates, and assigns them
- Includes more complex Horn clauses that bring multiple predicates together, for example "isPopularPopSong" combines both "popularSong" and "popSong". 

NOTE: This script will not work unless you have the MSD summary file locally in your project. The instructions mentioned not to include large files in our submission, so it is left out in the repo. You can access the million song dataset here: http://millionsongdataset.com/pages/getting-dataset/#subset

Just remember to name the file msd_summary_file.h5

## demo_krf_file.krf

The `.krf` file generated from `create_file.py`. Includes all the isa statements, definitions, predicates, Horn clauses, etc.

## msd_summary_file.h5

The file used to get data from the Million Song Database. For our purposes we only ever got 50 songs from this file, but you can get however many you want (up to a million, I suppose). You can change the number on line 157 of `create_file.py`.

NOTE: As mentioned above, you will need to get this file from http://millionsongdataset.com/pages/getting-dataset/#subset

## getsongs.py

Isn't used in our demo, but is an example script of specifically how we pulled songs from the Spotify API based on user input.