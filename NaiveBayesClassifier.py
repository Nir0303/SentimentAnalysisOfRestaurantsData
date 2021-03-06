import nltk 
import re
import numpy as np
import pandas 
from nltk.corpus import stopwords
import pickle
import os
import argparse
import re
import pandas as pd


stopWords = set(stopwords.words('english'))
specialCharacters = re.compile('[^a-zA-Z0-9 \n\.]')
word_features=None
def parse2(x,typ):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', x)
    t= cleantext.strip().split()
    s=[specialCharacters.sub('',i).lower() for i in t if len(i)>3]
    return (s,typ)

def parse(x):
	t= x.split('~')
	x=re.sub('\W+'," ",t[0])
	ta=x.split()
	s=[specialCharacters.sub('',i).encode('utf-8').lower() for i in ta if len(i)>3]
	return (s,t[1].split('\n')[0])


def filterValues(x):
    values=[]
    for i in x:
        if i!='i':
            values.append(re.sub('[^a-zA-Z0-9 \n\.]', '', i))
    return values



def extract_features(document):
	global word_features
	document_words = set(document)
	features = {}
	for word in word_features:
	  if word not in stopWords:
	    features['contains(%s)' % word] = (word in document_words)
	return features


def trainData():
    with open("data/IntegratedCons.txt") as IC:
	   combinedData=map(lambda x:parse2(x,'negative'),IC.readlines())
    with open("data/IntegratedCons.txt") as IC:
	   combinedData.extend(map(lambda x:parse2(x,'positive'),IC.readlines()))
    with open("data/reviewsR.txt") as IC:
	   combinedData.extend(map(lambda x:parse(x),IC.readlines()))
    words=[]
    for i in combinedData:
	    words.extend(i[0])
    dataFreq= nltk.FreqDist(tuple(words))
    global word_features
    word_features= dataFreq.keys()
    print dataFreq.most_common(10)
    training_set = nltk.classify.apply_features(extract_features,combinedData)
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    return classifier




parser = argparse.ArgumentParser()
parser.add_argument("--cached",help="wanted to use cache solution",action="store_true")
args = parser.parse_args()


if not os.path.isfile('output/NaiveBayesClassifier') or  not args.cached:
	naiveBayesClassifier = trainData()
	with open('output/NaiveBayesClassifier','wb') as classifier:
		pickle.dump(naiveBayesClassifier,classifier)

else:
	with open('output/NaiveBayesClassifier','rb') as classifier:
		naiveBayesClassifier = pickle.load(classifier)

print naiveBayesClassifier.show_most_informative_features(32)  

restaurantData = pd.read_csv('data/restaurantReviews.csv',delimiter="~")

restaurantData["tokenizedData"]=restaurantData["ReviewText"].str.lower().str.split().apply(lambda x: filterValues(x))

restaurantData["sentiment"]=restaurantData["tokenizedData"].apply(lambda x :naiveBayesClassifier.classify(extract_features(x)))


print restaurantData[:5]

restaurantData.to_csv('output/predicted.csv')
