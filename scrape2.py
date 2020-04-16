#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:22:41 2020

@author: jafetaparicio
"""

import os
import requests 
import urllib.request
from bs4 import BeautifulSoup
import bs4 as bs


path = '/Users/jafetaparicio/OneDrive - Eastern Connecticut State University/College/Spring2020/Thesis/Lyrics/songscraper/SongLists'

file = 'urls.txt'
with open(file) as infile :
        url = infile.readlines()
        infile.close()

for i, char in enumerate(url):
    url[i] = url[i].replace('\n', '')





sauce = urllib.request.urlopen(url[6])
soup = bs.BeautifulSoup(sauce, 'lxml')
table = soup.table
soup.find_all("table")[1]
    
nameFile = 'test'
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #row.append()
    
    with open(os.path.join(path, nameFile + ".txt")  , 'a') as f:
        f.write(", ".join(row))
        f.close()












#for i, char in enumerate(url):
#    sauce = urllib.request.urlopen(url[i])
#    soup = bs.BeautifulSoup(sauce, 'lxml')
#    table = soup.table
    
    
    
#    table_rows = table.find_all('tr')
 #   row = []
    
  #  for tr in table_rows:
   #     td = tr.find_all('td')
    #    row = [i.text for i in td]
        #row.append()
        
     #   with open(str(year)+'.txt', 'a') as f:
      #      f.write(", ".join(row))
       #     f.close()
            
            
#    year -= 1
    




