import logging
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

import pickle

from flask import request, jsonify

from codeitsuisse import app

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json();
    return jsonify(sentiment_analysis(data));


def sentiment_analysis(reviews):
    # cols = ['review', 'sentiment']
    # train_data = pd.read_csv('IMDB Dataset.csv', header=0, names=cols, encoding='ISO-8859-1')
    # train_text = train_data[['review']]
    loaded_model = joblib.load('train_model.sav')
    with open('vectorizer.pk', 'rb') as v:
        vectorizer = pickle.load(v)
    # tfidfvect = TfidfVectorizer().fit(train_text.review)
    response = []
    # for review in reviews:
    #     response.append((loaded_model.predict(vectorizer.transform(review))))
    response = list(loaded_model.predict(vectorizer.transform(reviews['reviews'])))
    return {'response': response}
