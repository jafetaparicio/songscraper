#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:16:30 2020

@author: jafetaparicio
"""

#get song name and artist from wikipedia
import os
import urllib.request
from bs4 import BeautifulSoup
import time

#partial url
url_year = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"
#songListDir = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Spring2020/Thesis/Lyrics/songscraper/SongLists'
songList_Dir = '/Users/jafetaparicio/Thesis/Lyrics/songscraper/SongLists'

    
for year in range(1960, 2020):
    sauce = urllib.request.urlopen(url_year + str(year))
    soup = BeautifulSoup(sauce, 'lxml')

    table = soup.find_all('table', {'class': 'wikitable'})[0]
    table_rows = table.find_all('tr')
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        
        with open(os.path.join(songList_Dir,  str(year)+'.txt'), 'a') as f:
            f.write("\t".join(row))
            f.close()
            
    #wait half second before next request
    time.sleep(.5)    
    








