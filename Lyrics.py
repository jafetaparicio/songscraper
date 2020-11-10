
# -*- coding: utf-8 -*-
 


import os
#Import the package and search for songs by a given artist:
import lyricsgenius
#import re
import time

path = "/Users/jafetaparicio/Thesis/Lyrics/songscraper/"
os.chdir(path)
songListDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLists'
songSearchDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongSearched'
searchDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongSearched'




#hide token
genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
songFile = '2019.txt'
year = 2019

def songLyrics(songFile, songListDir, songSearchDir, genius, year):

    with open(os.path.join(songListDir, songFile)) as infile :
        songList = infile.readlines()
        infile.close()
        
        songs = []
    for line in songList :
        line = line.strip("\"")
        line = line.strip("\n")
        line = line.strip("\"")
        songs.append(line.split("\t"))
        
 
    #Songs is new song list
    #Song title: songs[#][0]
    #Artist: songs[#][1]
        
    for i in range(0,100):
        print("Song Number: ", (i + 1))
        index = 0
        if len(songs[i]) > 2:
            index = 1
        getLyrics(songs[i][index].strip('"'), songs[i][index+1], songSearchDir, genius, year)
        
        print('\n')
        print("*********************************************")
        print("*********************************************")        
        print("*********************************************")
        print('\n')
        


def getLyrics(songName, artist, songSearchDir, genius, year):
    print("Getting:" ,songName, ' ******* ', artist)
    
    
    artist2 = genius.search_artist(artist, max_songs=1, sort="title")
    
    
    if artist2 == None:
        song = genius.search_song(songName)
    else:
        song = genius.search_song(songName, artist2.name)
    
    
    if song == None:
        with open(os.path.join(songSearchDir, 'error.txt'), 'a')  as f:
            f.write(songName + '\t' + artist + "\n")
            f.close()
        return 'null'
        #save to error file
    else:
        path = "/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLyrics/" + str(year) + '/'
        
        if os.path.isdir(path) == False:
            os.mkdir(path)
        try:   
            f= open(os.path.join(path, songName + '.txt') ,"w+")
        except FileNotFoundError as err:
            print('skipping:', err)
        f.write(song.lyrics)
        f.close()
        with open(os.path.join(songSearchDir, 'ActuallySearched' + str(year) +'.txt'), 'a')  as f:
            f.write(songName + '\t'+ artist + '\t*****\t' + song.title + '\t'  + song.artist + "\n")
            f.close()

    
    
    #wait half second before next request
    time.sleep(.5)
    return song

#for i in range(2019 ,2020):
#    songFile = str(year)+ '.txt'
#    songLyrics(songFile, songListDir, searchDir, genius, year)
#    year += 1
    
year = 2019
songFile = "2019.txt"
songLyrics(songFile, songListDir, searchDir, genius, year)
    



