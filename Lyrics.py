
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os


#Import the package and search for songs by a given artist:
import lyricsgenius

path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Spring2020/Thesis/Lyrics/"
os.chdir(path)



#genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
#artist = genius.search_artist("Andy Shauf", max_songs=1, sort="title")
#print(artist.songs)
#song = genius.search_song("To You", artist.name)
#print(song.lyrics)



def getLyrics(songName, artist):
    genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
    artist = genius.search_artist(artist, max_songs=1, sort="title")
    song = genius.search_song(songName, artist.name)
    if song == None:
        print("error")
        #save to error file
    else:
        f= open(songName + '.txt' ,"w+")
        f.write(song.lyrics)
        f.close()
    
    
getLyrics("Truth Hurts", "Lizzo")



#Search for a single song by the same artist:
#artist.add_song(song)

#add the song to the artist object
#artist.add_song(song)

#Save the artist's songs to a JSON file:
#artist.save_lyrics()










