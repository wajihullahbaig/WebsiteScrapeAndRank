#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:54:45 2021

@author: wajih
"""
import os,sys
sys_path = sys.path
path = os.getcwd()
path = os.path.split(path)[0]
last_part = os.path.split(path)[1] 
if path not in sys_path:
    sys.path.insert(1, path)

import os

import requests
from Analyzers.TextAnalyzer import TextAnalyzer
from Analyzers.HtmlStripper import HtmlStripper

    
class WebsiteRetriever:
    headers = None
    def __init__(self):
        self.headers = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0 ",
        "Referer": "https://pamirtours.pk/",
        "Host": "pamirtours.pk",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding":	"gzip, deflate, br",
        "Connection": "keep-alive"
            } 
    
    def process(self,url):
        try:            
            r = requests.get(url,self.headers)
            if r.status_code == 200:
                return {r.status_code:r.content}
            else:
                return {r.status_code:None}        
        except Exception as e:
            print("We have an error", e)
            return None

class URLAnalyzer (TextAnalyzer): 
    wr = WebsiteRetriever()
    hs = HtmlStripper()
    def __init__ (self):
        TextAnalyzer.__init__(self)    
    def process(self,url):
        response = self.wr.process(url)        
        if response:
            if 200 in response:
                html = response[200]
                if html:
                    if html != '':
                        text = self.hs.process(html)
                        if text:
                            word_cloud,top_words,top2_words,top3_words,top_df,top2_df,top3_df,score_sorted_keywords = super().process(text)
                            return word_cloud,top_words,top2_words,top3_words,top_df,top2_df,top3_df,score_sorted_keywords
                        else:
                            return None,None,None,None,None,None,None,None
        return None,None,None,None,None,None,None,None
            
    