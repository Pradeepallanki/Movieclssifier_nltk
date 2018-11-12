#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:02:43 2018

@author: pradi
"""
import nltk
import random
from nltk.corpus import movie_reviews

documents=[]
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
allwords=[]

for w in movie_reviews.words():
   allwords.append(w.lower());

allwords=nltk.FreqDist(allwords)

word_features=list(allwords.keys())[:3000]

print(type(word_features[0]))


def find(document):
    words=set(document)
    words=list(words) 
    features={}
 
    for w in word_features:
        features[w]=(w in words)
    return features


fetset=find(movie_reviews.words('neg/movie.txt')) # you can input your file here, but make sure that file is stored inside /home/user/nltk_data/corpora/movie_reviews/ 
falsecount=0;
truecount=0;

for key in fetset:
    if(fetset[key] ==True):
        truecount+=1
    else:
        falsecount+=1
if(falsecount>truecount):
    print("Classified negatively");
else:
    print("Classified positively");
 





        



