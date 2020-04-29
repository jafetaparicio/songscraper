
# -*- coding: utf-8 -*-
 


import os
#Import the package and search for songs by a given artist:
import lyricsgenius
import re

path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Spring2020/Thesis/Lyrics/"
os.chdir(path)



#genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
#artist = genius.search_artist("Andy Shauf", max_songs=1, sort="title")
#print(artist.songs)
#song = genius.search_song("To You", artist.name)
#print(song.lyrics)


songListDir = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Spring2020/Thesis/Lyrics/songscraper/SongLists'
os.path.join(songListDir, '2019.txt')
#reading url file and creating list
file = '2019.txt'
with open(os.path.join(songListDir, '2019.txt')) as infile :
        songList = infile.readlines()
        infile.close()
        
        

for line in songList:
    songs = line.split("\t")
    


    

    
songs[0] = songs[0].strip("\"")
songs[1] = songs[1].strip("\n")

'''
#file of song name and artist searched and year(hot100), and song name and artist actually searched and year
'''
#add year param
def getLyrics(songName, artist, year):
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
        #log file .txt or csv, seperate by a tab
    #wait half second before next request
    time.sleep(.5)
    return song
    
    
s = getLyrics("Te quiero", "Lizzo")



