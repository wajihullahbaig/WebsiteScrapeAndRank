#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 14:40:23 2021

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
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
import io
import re
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 
from scipy.sparse import coo_matrix
from Analyzers.HtmlStripper import HtmlStripper
             


class TextAnalyzer:
    stop_words = None
    hs = HtmlStripper()
    def __init__(self):
        # You only need to download these resources once. After you run this
        # the first time--or if you know you already have these installed--
        # you can comment these two lines out (with a #)
        nltk.download('stopwords')
        nltk.download('wordnet')
        # Create a list of stop words from nltk
        self.stop_words = set(stopwords.words("english"))        

    def process(self,text):
        cleaned_text = self.hs.process(text)
        cleaned_text,ds_count = self.clean_text(cleaned_text)
        self.generate_word_cloud(cleaned_text)
        word_cloud = self.generate_word_cloud(cleaned_text)
        
        top_words = self.get_top_n_words(cleaned_text)
        top_df = pd.DataFrame(top_words)
        top_df.columns=["Keyword", "Frequency"]
        
        top2_words = self.get_top_n2_words(cleaned_text)
        top2_df = pd.DataFrame(top2_words)
        top2_df.columns=["Bi-gram", "Frequency"]
        
        top3_words = self.get_top_n3_words(cleaned_text)
        top3_df = pd.DataFrame(top3_words)
        top3_df.columns=["Tri-gram", "Frequency"]
    
        X,cv_model = self.count_vectorize(cleaned_text)
        tf_idf_vector = self.get_tfidf(X, cv_model, cleaned_text, ds_count)
        # Sort the tf-idf vectors by descending order of scores
        sorted_items=self.sort_coo(tf_idf_vector.tocoo())    
        # Get feature names
        feature_names=cv_model.get_feature_names()    
        # Extract only the top n; n here is 25
        score_sorted_keywords=self.extract_topn_from_vector(feature_names,sorted_items,25)
        tfidf = pd.Series(score_sorted_keywords, name='score')
        tfidf.index.name = "keywords"
        return word_cloud,top_words,top2_words,top3_words,top_df,top2_df,top3_df,tfidf
    
    def replace_all(self, text, stop_words):
        for s in stop_words:
            text = re.sub(s.center(len(s)+2), "", text)
        return text
    
    def clean_text(self,text):
        
        # Load a set of custom stop words from a text file (one stopword per line)
        #csw = set(line.strip() for line in open('custom-stopwords.txt'))
        #csw = [sw.lower() for sw in csw]
        # print(sorted(csw))

        # Combine custom stop words with stop_words list
        #stop_words = stop_words.union(csw)
        # print(sorted(stop_words))
        dataset = pd.DataFrame({"text": [text]})
        dataset.head()

        # Pre-process dataset to get a cleaned and normalised text corpus
        datacol = "text"
        dataset['word_count'] = dataset[datacol].apply(
            lambda x: len(str(x).split(" ")))
        ds_count = len(dataset.word_count)
        # Remove punctuation
        text = re.sub('[^a-zA-Z]', ' ', text)
        # Convert to lowercase
        text = text.lower()

        # Remove tags
        text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)

        # Remove special characters and digits
        #text=re.sub("(\\d|\\W)+"," ",text)

        # Remove special characters
        import string
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove stop words
        text = self.replace_all(text, list(self.stop_words))

        # Convert to list from string - double white space is important!
        text = text.split("  ")
        text = [i.strip(' ') for i in text]
        text = [x for x in text if len(x.strip()) > 0]
        # Stemming
        #ps = PorterStemmer()

        # Lemmatisation
        lem = WordNetLemmatizer()
        text = [lem.lemmatize(word) for word in text if not word in self.stop_words]
        return text,ds_count
    
    def generate_word_cloud(self,text):
        wordcloud = WordCloud(
                                  background_color='white',
                                  stopwords=self.stop_words,
                                  max_words=100,
                                  max_font_size=50, 
                                  random_state=42
                                 ).generate(str(text))
        return wordcloud

    def count_vectorize(self,text):       
        cv=CountVectorizer(max_df=0.8,stop_words=self.stop_words, max_features=10000, ngram_range=(1,3))
        X=cv.fit_transform(text)      
        # Sample the returned vector encoding the length of the entire vocabulary
        #list(cv.vocabulary_.keys())[:10]
        return X,cv
    
    # View most frequently occuring keywords
    def get_top_n_words(self,corpus, n=25):
        vec = CountVectorizer().fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in      
                       vec.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], 
                           reverse=True)
        return words_freq[:n]
    
    
    # Most frequently occuring bigrams
    def get_top_n2_words(self,corpus, n=25):
        vec1 = CountVectorizer(ngram_range=(2,2),  
                max_features=2000).fit(corpus)
        bag_of_words = vec1.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in     
                      vec1.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], 
                    reverse=True)
        return words_freq[:n]
    
    
    # Most frequently occuring Tri-grams
    def get_top_n3_words(self,corpus, n=25):
        vec1 = CountVectorizer(ngram_range=(3,3), 
               max_features=2000).fit(corpus)
        bag_of_words = vec1.transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in     
                      vec1.vocabulary_.items()]
        words_freq =sorted(words_freq, key = lambda x: x[1], 
                    reverse=True)
        return words_freq[:n]
    
    
    def get_tfidf(self,X,cv,corpus,ds_count):
        # Get TF-IDF (term frequency/inverse document frequency) -- 
        # TF-IDF lists word frequency scores that highlight words that 
        # are more important to the context rather than those that 
        # appear frequently across documents
        
        tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
        tfidf_transformer.fit(X)
        
        # Get feature names
        feature_names=cv.get_feature_names()
         
        # Fetch document for which keywords needs to be extracted
        doc=corpus[ds_count-1]
         
        # Generate tf-idf for the given document
        tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))
        return tf_idf_vector
        
    # Sort tf_idf in descending order
    def sort_coo(self,coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
     
    def extract_topn_from_vector(self,feature_names, sorted_items, topn=25):
        
        # Use only topn items from vector
        sorted_items = sorted_items[:topn]
        score_vals = []
        feature_vals = []
        
        # Word index and corresponding tf-idf score
        for idx, score in sorted_items:
            
            # Keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])
     
        # Create tuples of feature,score
        # Results = zip(feature_vals,score_vals)
        results= {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]]=score_vals[idx]
        return results
    
