
# -*- coding: utf-8 -*-
 


import os
#Import the package and search for songs by a given artist:
import lyricsgenius
import re
import time

path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/"
os.chdir(path)
songListDir = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongLists'
songSearchDir = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongSearched'
searchDir = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongSearched'

#with open(os.path.join(songListDir, '2019.txt')) as infile :
#        songList = infile.readlines()
#        infile.close()
#        
#songs = []
#
#for line in songList :
#    line = line.strip("\"")
#    line = line.strip("\n")
#    line = line.strip("\"")
#    songs.append(line.split("\t"))
#    
##Songs is new song list
##Song title: songs[#][0]
##Artist: songs[#][1]
#
#
#
##file of song name and artist searched and year(hot100), and song name and artist actually searched and year
#
##keep off git
#genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
#artist = genius.search_artist(songs[98][1], max_songs=1, sort="title")
#song = genius.search_song(songs[98][0], songs[98][1])
#
#with open(os.path.join(songSearchDir, 'search.txt'), 'a')  as f:
#    f.write(songs[98][0] + ' '+ songs[98][1] + ' ****** ' +song.title + ' '  + song.artist + "\n")
#    f.close()


genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")

file = '2018.txt'
year = 2018
count = 1

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
        getLyrics(songs[i][0].strip('"'), songs[i][1], songSearchDir, genius, year)
        
        
        


#add year param
def getLyrics(songName, artist, songSearchDir, genius, year, count):
    print("Song Number: ", count)
    print("Getting:" ,songName, ' *** ', artist)
    
    
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
        path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongLyrics/" + str(year) + '/'
        
        if os.path.isdir(path) == False:
            os.mkdir(path)
            
        f= open(os.path.join(path, songName + '.txt') ,"w+")
        f.write(song.lyrics)
        f.close()
        with open(os.path.join(songSearchDir, 'ActuallySearched.txt'), 'a')  as f:
            f.write(songName + '\t'+ artist + '\t*****\t' + song.title + '\t'  + song.artist + "\n")
            f.close()
                
#        else:
#            os.mkdir(str(year))
#            path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongLyrics/" + str(year) + '/'
#            os.chdir(path)
#        
#            f= open(songName + '.txt' ,"w+")
#            f.write(song.lyrics)
#            f.close()
            #log file .txt or csv, seperate by a tab
    
#        with open(os.path.join(songSearchDir, 'ActuallySearched.txt'), 'a')  as f:
#            f.write(songName + '\t'+ artist + '\t*****\t' + song.title + '\t'  + song.artist + "\n")
#            f.close()
    
    
    #wait half second before next request
    time.sleep(.5)
    count += 1 
    return song





#################################################################################################################################

#def getLyrics(songName, artist, songSearchDir, genius, year):

#artist = 'Drake'
#songName = 'Gods Plan'
#songSearchDir = searchDir
#genius = lyricsgenius.Genius("eNHgmMCeRrd8prhC7EnyZtxX6Y_Ek8HOjMq8AS_6WCX4aiRhiqQiXYDukJcgyZcb")
#
#print("getting:" ,songName, ' *** ', artist)
#    
#    
#artist2 = genius.search_artist(artist, max_songs=1, sort="title")
#    
#    
#if artist2 == None:
#    song = genius.search_song(songName)
#else:
#    song = genius.search_song(songName, artist2)
#    
#    
#if song == None:
#    with open(os.path.join(songSearchDir, 'error.txt'), 'a')  as f:
#        f.write(songName + '\t' + artist + "\n")
#        f.close()
#    return 'null'
#        #save to error file
#else:
#    path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/SongLyrics/" + str(year) + '/'
#        
#    if os.path.isdir(path) == False:
#        os.mkdir(path)
#            
#    f= open(os.path.join(path, songName + '.txt') ,"w+")
#    f.write(song.lyrics)
#    f.close()
#    with open(os.path.join(songSearchDir, 'ActuallySearched.txt'), 'a')  as f:
#        f.write(songName + '\t'+ artist + '\t*****\t' + song.title + '\t'  + song.artist + "\n")
#        f.close()






#################################################################################################################################

songLyrics(file, songListDir, searchDir, genius, year)
#path = "/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/"
#os.chdir(path)
#
#artist = 'Drake'
#songName = 'Gods Plan'
#
#artist2 = genius.search_artist(artist, max_songs=1, sort="title")
#genius.search_song(songName, artist2, get_full_info = False)

