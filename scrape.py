#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:16:30 2020

@author: jafetaparicio
"""

#get song name and artist from wikipedia

import os
import requests 
import urllib.request
from bs4 import BeautifulSoup

url ="https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2019"
site = requests.get(url)

html_content = site.text

#creating soup object
soup = BeautifulSoup(html_content, "html.parser")

for tr in soup.find_all('tr')[2]:
    tds = soup.find_all('td')
    print("Number: %s, Title: %s, Artist(s): %s\n"%(tds[0].text,tds[1].text,tds[2].text))
    
