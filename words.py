#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from textblob import TextBlob
import re
from collections import Counter
#import nltk
#nltk.download('punkt')

path ="/Users/jafetaparicio/Lyrics/"
lyricsPath ="/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Fall2020/Thesis/Lyrics/Clout.txt"
songListDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLists'
songSearchDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongSearched'
songSentiment ='/Users/jafetaparicio/Thesis/Lyrics/songscraper/Sentiment'
wordsPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/Words'
uniquePath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords'

songFile = '1960.txt'
year = 1960

def removeBrackets(x) :

    """Returns 'x' with bracket content removed"""
    r = re.sub('\[.+?\]', '', x)
    return r


def getWords(year,path,songFile,songListDir):
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
        words = set()
        index = 0
        if len(s) > 2:
            index = 1
    
        path = "/Users/jafetaparicio/Lyrics/" +str(year)+'/' + s[index].strip('"') + '.txt'
        
        try:
            with open(path) as infile:
                lyrics = infile.readlines()
        except FileNotFoundError as er:
            print("exception", er)
            
    
        for line in lyrics :
            line = line.strip("\n")
            line = line.strip("\"")
            line = line.strip("\"")
            line = removeBrackets(line)
            
            if line != '' :
                w = TextBlob(line).words
                for w1 in w:  
                    words.add(w1)
         
#        unique = Counter(words)
#        tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/Words/' + str(year) + '/'
        tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords/' + str(year) + '/'
        if os.path.isdir(tempPath) == False:
                os.mkdir(tempPath)
        try:          
            f= open(os.path.join(tempPath, str(s[index]) + '.txt') ,'a')
            for w in words:
                f.write(w + '\n')
#            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
#            f.write(str(unique)) # t¡his writes the unique words count to a text file
            f.close()
        except FileNotFoundError as er:
            print("exception", er) 
        
year = 1960
for i in range(1960 ,2020):
    songFile = str(year)+ '.txt'
    getWords(year,path,songFile,songListDir)
    year += 1











#wordsList = []
#year = 2019
#songFile = '2019.txt'
#
with open(os.path.join(uniquePath)) as infile :
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
    words = set()
    index = 0
    if len(s) > 2:
        index = 1

    path = "/Users/jafetaparicio/Lyrics/" +str(year)+'/' + s[index].strip('"') + '.txt'
    
    try:
        with open(path) as infile:
            lyrics = infile.readlines()
    except FileNotFoundError as er:
        print("exception", er)
        

    for line in lyrics :
        line = line.strip("\n")
        line = line.strip("\"")
        line = line.strip("\"")
        line = removeBrackets(line)
        
        if line != '' :
            w = TextBlob(line).words
            for w1 in w:  
                #if w1 not in stopwords :
                words.add(w1)
     
#        unique = Counter(words)
#        tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/Words/' + str(year) + '/'
    tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords/' + str(year) + '/'
    if os.path.isdir(tempPath) == False:
            os.mkdir(tempPath)
    try:          
        f= open(os.path.join(tempPath, str(s[index]) + '.txt') ,'a')
        for w in words:
            f.write(w + '\n')
#            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
#            f.write(str(unique)) # t¡his writes the unique words count to a text file
        f.close()
    except FileNotFoundError as er:
        print("exception", er)
        
        
        
        
year= 1960
tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords/' + str(year) + '/'
files = os.listdir(tempPath)
f = files[0]

allwords = []
for f in files :
    with open(tempPath + f) as fin :
        words = fin.readlines()
        words = [w.lower().strip() for w in words]
        allwords += words


counts = Counter(allwords)


# get top 10 words
counts.most_common(10)



















