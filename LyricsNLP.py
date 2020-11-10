#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:38:45 2020

@author: jafetaparicio
"""

import os
from textblob import TextBlob
import re
import nltk
import lyricsgenius

#nltk.download('punkt')

path ="/Users/jafetaparicio/Lyrics/"
lyricsPath ="/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/Clout.txt"
songListDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLists'
songSearchDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongSearched'
songSentiment ='/Users/jafetaparicio/Thesis/Lyrics/songscraper/Sentiment'
wordsPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/Words'

songFile = '2019.txt'
year = 2019

#lyricsPath = "/Users/jafetaparicio/Documents/Lyrics/2019/Clout.txt"
#songListDir = '/Users/jafetaparicio/Documents/Lyrics/2019/Clout.txt'
#lyricsFile = '/Users/jafetaparicio/Documents/Lyrics/2019'
lyricsFile = 'Clout.txt'



def removeBrackets(x) :

    """Returns 'x' with bracket content removed"""
    r = re.sub('\[.+?\]', '', x)
    return r



def getPol(year, path,songFile, songListDir):
    with open(os.path.join(songListDir, songFile)) as infile :
        songList = infile.readlines()
        infile.close()
        
    songs = []
    for line in songList :
        line = line.strip("\"")
        line = line.strip("\n")
        line = line.strip("\"")
        songs.append(line.split("\t"))
        
    for i,s in enumerate(songs):
        print("Song Number: ", (i + 1))
        index = 0
        if len(s) > 2:
            index = 1
#        print(songs[i][index].strip('"'))
    
        path = "/Users/jafetaparicio/Lyrics/" +str(year)+'/' + s[index].strip('"') + '.txt'
        
        try:
            with open(path) as infile:
                lyrics = infile.readlines()
        except FileNotFoundError as er:
            print("exception", er)
    
        polarityCount = 0
        for line in lyrics :
            line = line.strip("\"")
            line = line.strip("\n")
            line = line.strip("\"")
            line = removeBrackets(line)
            numLines = 0
    
            if line != '' :
                sent = TextBlob(line).sentiment.polarity
                polarityCount = sent + polarityCount
                numLines += 1




#if numlines is 0 for instrumental handle it
        if numLines == 0:
            numLines = 1
        polarityCount = polarityCount/numLines
        print(polarityCount)
        f= open(os.path.join(songSentiment, str(year) + '.txt') ,'a')
        f.write(str(i) + '\t' +str(polarityCount)+ '\n')
        f.close()
        
        
        
        



year = 1960
for i in range(1960 ,2020):
    songFile = str(year)+ '.txt'
    getPol(year,path,songFile,songListDir)
    year += 1
    








        
   
