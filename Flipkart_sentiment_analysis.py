# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:01:22 2024

@author: shubh
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as pgo
import tensorflow as tf 

#importing data set

dataset = pd.read_csv('flipkart.csv')

print(dataset.head())
# Checking if data set has null values 
print(dataset.isnull().sum())

#cleaning the data 
import re 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]) # thats the colum one where it has review
    review = review.lower() # converts all the cases into lower cases
    review = review.split() # splits the words in each review
    ps = PorterStemmer() # change like: loved to love
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)
dataset['Review']= corpus


# findin the pi chart for rating
rating = dataset["Rating"].value_counts()
Index = rating.index
Values_sum = rating.values 
fig = px.pie(dataset, values= Values_sum, names=Index)
fig.show()
fig.write_image("Rating.png")


### sentiment analsysis model
# VADER-Sentiment-Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
compound_score = []
compound_score_all = []
for j in range(0,len(dataset)):
    sentiment_score= analyzer.polarity_scores(dataset['Review'][j])   
    compound_score.append( sentiment_score["compound"]) #extreacting 
    compound_score_all.append(sentiment_score) #extreacting 

sentiment_values=[0]*3
sentiment_value_index = ["Positive","Negative", "Neutral"]
sentiments=[0]*len(compound_score)
for i in range(0,len(compound_score)):
    if compound_score[i]>=0.05:
        sentiment_values[0] = sentiment_values[0]+1 
        sentiments[i]= 'Positive'
    elif compound_score[i]<=-0.05:
         sentiment_values[1] = sentiment_values[1]+1   
         sentiments[i]= 'Negative'
    else:     
         sentiment_values[2] = sentiment_values[2]+1 
         sentiments[i]= 'Neutral'



fig = px.pie(dataset, values= sentiment_values, names=sentiment_value_index)
fig.show()
fig.write_image("Sentiments.png")
