#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:52:48 2021

@author: wajih
"""

import os,sys
sys_path = sys.path
path = os.getcwd()
path = os.path.split(path)[0]
last_part = os.path.split(path)[1] 
if path not in sys_path:
    sys.path.insert(1, path)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from Analyzers.URLAnalyzer import URLAnalyzer;

url = "https://netflix.com/"

anaylzer = URLAnalyzer()
word_cloud,top_words,top2_words,top3_words,top_df,top2_df,top3_df,score_sorted_keywords = anaylzer.process(url)
# Check one entry to see if we have something
if word_cloud:
    print(word_cloud)
    fig = plt.figure(1)
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
    #    fig.savefig(output_path+file_prefix + "wordcloud.png", dpi=900)
     
    
    # Convert most freq words to dataframe for plotting bar plot, save as CSV
    print(top_df.to_markdown())
    # Barplot of most freq words
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Keyword", y="Frequency", data=top_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    plt.show()
    
    print(top2_df.to_markdown())
    # Barplot of most freq words
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Bi-gram", y="Frequency", data=top2_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    plt.show()
    
    print(top3_df.to_markdown())
    # Barplot of most freq words
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Tri-gram", y="Frequency", data=top3_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    plt.show()
    df = pd.Series(score_sorted_keywords, name='tf-df score')
    df.index.name = "keywords"
    print(df.to_markdown())