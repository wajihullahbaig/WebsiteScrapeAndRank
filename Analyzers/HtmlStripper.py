#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 08:43:14 2021

@author: wajih
"""
import os,sys
sys_path = sys.path
path = os.getcwd()
path = os.path.split(path)[0]
last_part = os.path.split(path)[1] 
if path not in sys_path:
    sys.path.insert(1, path)
    
from bs4 import BeautifulSoup

class HtmlStripper:
    soup = None
    def __init__(self):    
        pass

    def process(self,html):               
        self.soup = BeautifulSoup(html, "html.parser") # create a new bs4 object from the html data loaded            
        for script in self.soup(["script", "style"]): # remove all javascript and stylesheet code
            script.extract()
        # get text
        text =self. soup.get_text(" ") # retain white spaces
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text