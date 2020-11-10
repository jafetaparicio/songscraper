#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from textblob import TextBlob
import re
from collections import Counter
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')

path ="/Users/jafetaparicio/Lyrics/songscraper/SongLyrics"
#lyricsPath ="/Users/jafetaparicio/Thesis/Lyrics/Clout.txt"
songListDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLists'
songSearchDir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongSearched'
songSentiment ='/Users/jafetaparicio/Thesis/Lyrics/songscraper/Sentiment'
wordsPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/Words'
uniquePath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords'
topWords = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/TopWords'
topArtist = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/TopArtist'

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
            continue
    
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
                
                
                
                
        print(s[index], words)        
        
        try:          
            f= open(os.path.join(tempPath, str(s[index]) + '.txt') ,'a')
            for w in words:
                f.write(w + '\n')
#            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
#            f.write(str(unique)) # t¡his writes the unique words count to a text file
            f.close()
        except FileNotFoundError as er:
            print("exception", er) 
        
year = 2019
for i in range(2019,2020):
    songFile = str(year)+ '.txt'
    getWords(year,path,songFile,songListDir)
    year += 1











wordsList = []
year = 2019
songFile = '2019.txt'

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
                words.add(w1.lower())
     
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
stop_words = set(stopwords.words('english')) 

allwords = []

with open(tempPath + f) as fin :
        words = fin.readlines()
        words = [w.lower().strip() for w in words]
        allwords += words
#        word_tokens = word_tokenize(words)
#        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
filtered_words = [w for w in allwords if not w in stop_words] 
        


counts = Counter(filtered_words)

# get top 10 words
top = counts.most_common(10)

tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/TopWords/' + str(year) + '/'
if os.path.isdir(tempPath) == False:
        os.mkdir(tempPath)
try:          
    f= open(os.path.join(tempPath, f) ,'a')
    for w in top:
        f.write(str(w) + '\n')
#            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
#            f.write(str(unique)) # t¡his writes the unique words count to a text file
    f.close()
except FileNotFoundError as er:
    print("exception", er)








for f in files :
    print(f)
    allwords = []
    with open(tempPath + f) as fin :
        words = fin.readlines()
        words = [w.lower().strip() for w in words]
        allwords += words
    #        word_tokens = word_tokenize(words)
    #        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_words = [w for w in allwords if not w in stop_words] 
            
    
    
    counts = Counter(filtered_words)
    
    # get top 10 words
    top = counts.most_common(10)
    
    tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/TopWords/' + str(year) + '/'
    if os.path.isdir(tempPath) == False:
            os.mkdir(tempPath)
    try:          
        f= open(os.path.join(tempPath, f) ,'a')
        for w in top:
            f.write(str(w) + '\n')
    #            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
    #            f.write(str(unique)) # t¡his writes the unique words count to a text file
        f.close()
    except FileNotFoundError as er:
        print("exception", er)






    year+=1

def topWords(tempPath, f, year):
    stop_words = set(stopwords.words('english')) 
    print(f)
    allwords = []
    with open(tempPath + f) as fin :
        words = fin.readlines()
        words = [w.lower().strip() for w in words]
        allwords += words
    #        word_tokens = word_tokenize(words)
    #        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_words = [w for w in allwords if not w in stop_words] 
            
    
    
    counts = Counter(filtered_words)
    
    # get top 10 words
    top = counts.most_common(10)
    
    tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/TopWords/' + str(year) + '/'
    if os.path.isdir(tempPath) == False:
            os.mkdir(tempPath)
    try:          
        f= open(os.path.join(tempPath, f) ,'a')
        for w in top:
            f.write(str(w) + '\n')
    #            f.write(str(words)) # this is to w¡¡rite just the words to a file¡¡
    #            f.write(str(unique)) # t¡his writes the unique words count to a text file
        f.close()
    except FileNotFoundError as er:
        print("exception", er)


year = 1998
for i in range(1998,2019):
    tempPath = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/UniqueWords/' + str(year) + '/'
    files = os.listdir(tempPath)
    for f in files:
        topWords(tempPath,f, year)
    year+=1
    







###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################


songFile = "1960.txt"
year = 1960



def topArtist(songFile, songListDir, year):
    artist = []
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
        print(songs[i][index].strip('"')) #songname
        print(songs[i][index+1]) #artist
        artist.append(songs[i][index+1])
    counts = Counter(artist)
    print("These are the top artist of year " + str(year))
    print(counts)    
        
    print('\n')
    print("*********************************************")
    print("*********************************************")        
    print("*********************************************")
    print('\n')

topArtist(songFile, songListDir, year)




