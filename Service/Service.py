#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:43:51 2021

@author: wajih
"""

import os,sys
sys_path = sys.path
path = os.getcwd()
path = os.path.split(path)[0]
last_part = os.path.split(path)[1] 
if path not in sys_path:
    sys.path.insert(1, path)
    
from Analyzers.TextAnalyzer import TextAnalyzer
import datetime
import uuid
from flask import Flask, render_template, request, redirect, url_for,send_from_directory,send_file
import io
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import traceback
import shutil
import zipfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.html', '.htm', '.txt']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['DOWNLOAD_PATH'] = 'downloads'


def zip_results(results,output_path):
    for k,v in results.items():
        v.to_csv(output_path+"/"+k+".csv")
    shutil.make_archive(output_path, 'zip',output_path)
    
def do_plots(word_cloud,top_words,top2_words,top3_words,top_df,top2_df,top3_df,score_sorted_keywords):    
    print("Inside do_plots")
    fig = plt.figure(1)
    plt.imshow(word_cloud)
    plt.axis('off')
    word_cloud_str = io.BytesIO()
    #plt.show()
    fig.savefig(word_cloud_str,format='png')    
    #fig.savefig(output_path+file_prefix + "wordcloud.png", dpi=900)
    plt.close(fig)
    word_cloud_str.seek(0)
    word_cloud_base64 = base64.b64encode(word_cloud_str.getvalue()).decode('ascii')
    word_cloud_str.close()
        
    # Convert most freq words to dataframe for plotting bar plot, save as CSV
    # Barplot of most freq words
    fig = plt.figure(1)
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Keyword", y="Frequency", data=top_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)    
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    top_str = io.BytesIO()
    fig.savefig(top_str,format='png')
    #plt.show()
    plt.close(fig)
    top_str.seek(0)
    top_str_base64 = base64.b64encode(top_str.getvalue()).decode('ascii')
    top_str.close()
    
    # Barplot of most freq words
    fig = plt.figure(1)    
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Bi-gram", y="Frequency", data=top2_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    top2_str = io.BytesIO()
    fig.savefig(top2_str,format='png')
    #plt.show()
    plt.close(fig)
    top2_str.seek(0)
    top2_str_base64 = base64.b64encode(top2_str.getvalue()).decode('ascii')
    top2_str.close()
    
    # Barplot of most freq words
    fig = plt.figure(1)            
    sns.set(rc={'figure.figsize':(13,8)})
    g = sns.barplot(x="Tri-gram", y="Frequency", data=top3_df, palette="Blues_d")
    g.set_xticklabels(g.get_xticklabels(), rotation=45)
    #g.figure.savefig(output_path+file_prefix + "_keyword.png", bbox_inches = "tight")
    top3_str = io.BytesIO()
    fig.savefig(top3_str,format='png')    
    #plt.show()
    plt.close(fig)
    top3_str.seek(0)
    top3_str_base64 = base64.b64encode(top3_str.getvalue()).decode('ascii')
    top3_str.close()
    
    df = pd.Series(score_sorted_keywords, name='score')
    df.index.name = "keywords"
    
    return word_cloud_base64,top_str_base64,top2_str_base64,top3_str_base64
    

def process_file(input_file):
    ta = TextAnalyzer()
    print("Inside process_file")
    word_cloud,top_words,top2_words,\
        top3_words,top_df,top2_df,top3_df,\
            score_sorted_keywords = ta.process(text = input_file);    
                        
    wcb64,tb64,t2b64,t3b64 = do_plots(word_cloud, top_words, top2_words, top3_words, top_df, top2_df, top3_df, score_sorted_keywords)        
    results_for_zip = {}
    results_for_zip["top_df"] = top_df
    results_for_zip["top2_df"] = top2_df
    results_for_zip["top3_df"] = top3_df
    results_for_zip["score_sorted_keywords"] = score_sorted_keywords

    results_for_views = {}
    results_for_views["wcb64"] = wcb64
    results_for_views["tb64"] = tb64
    results_for_views["t2b64"] = t2b64
    results_for_views["t3b64"] = t3b64

    return results_for_views,results_for_zip



@app.route('/')
def index():
    return render_template('index.html')

def create_paths_and_names(filename):
    dt_str = str(datetime.datetime.now()).replace(":", "-").replace(".", "_")            
    os.mkdir(app.config['UPLOAD_PATH']+'/'+dt_str)
    file_upload_path = app.config['UPLOAD_PATH']+'/'+dt_str+"/"+filename
    zip_download_path = app.config['DOWNLOAD_PATH']+'/'+dt_str
    return dt_str,file_upload_path,zip_download_path        
    
@app.route('/file_upload_anaylsis', methods=['POST'])
def process_uploaded_file():
    try:
        print("Recieved request at:",str(datetime.datetime.now()),flush=True)
        uploaded_file = request.files['html_file']
        if uploaded_file.filename != '':
            dt_str,file_upload_path,zip_download_path = create_paths_and_names(uploaded_file.filename)
            os.mkdir(app.config['DOWNLOAD_PATH']+'/'+dt_str)
            print(f"Saving uploaded file: {uploaded_file.filename}",flush=True)        
            uploaded_file.save(file_upload_path)  
            f = open(file_upload_path)              
            input_file = f.read()
            f.close()
            os.remove(file_upload_path)
            results,results_for_zip = process_file(input_file)            
            zip_results(results_for_zip,zip_download_path)            
            print("Process_file complete, rendering results.")
            #shutil.rmtree(app.config['UPLOAD_PATH']+'/'+dt_str)            
            return render_template('results.html', wcb64=results["wcb64"],tb64=results["tb64"],t2b64=results["t2b64"],t3b64=results["t3b64"],zipfile_link=dt_str+".zip")
    except :
        traceback.print_exc(file=sys.stdout)
    return redirect(url_for('index'))

    
@app.route('/text_upload_analysis', methods=['POST'])
def process_uploaded_text():
    try:
        print("Recieved request at:",str(datetime.datetime.now()),flush=True)
        uploaded_text = request.form['uploaded_text']
        if uploaded_text != '':
            filename = str(uuid.uuid4().hex)
            print(f"Create name as{filename}")            
            dt_str,_,zip_download_path = create_paths_and_names(filename)
            os.mkdir(app.config['DOWNLOAD_PATH']+'/'+dt_str)
            results,results_for_zip = process_file(uploaded_text)            
            zip_results(results_for_zip,zip_download_path)            
            print("Process_file complete, rendering results.")
            #shutil.rmtree(app.config['UPLOAD_PATH']+'/'+dt_str)            
            return render_template('results.html', wcb64=results["wcb64"],tb64=results["tb64"],t2b64=results["t2b64"],t3b64=results["t3b64"],zipfile_link=dt_str+".zip")
    except :
        traceback.print_exc(file=sys.stdout)
    return redirect(url_for('index'))



    
@app.route( '/'+app.config['DOWNLOAD_PATH']+'/'+'<filename>', methods=['GET'])
def downloads(filename):
    return send_file(app.config['DOWNLOAD_PATH']+'/'+filename,as_attachment=True)


if __name__ == '__main__':     
    app.run(host='0.0.0.0', port=8001, debug=False)    
