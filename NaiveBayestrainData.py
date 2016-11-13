# -*- coding: utf-8 -*-
import nltk 
import re
global word_features
def parse_second(x,typ):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', x)
    t= cleantext.strip().split()
    s=[i for i in t if len(i)>3]
    return (s,typ)

def parse(x):
	t= x.split('~')
	x=re.sub('\W+'," ",t[0])
	ta=x.split()
	s=[i.encode('utf-8').lower() for i in ta if len(i)>3]
	#print x
	return (s,t[1].split('\n')[0])
negFileVar="C:\Users\Niran0303\Google Drive\Hackrpi\New folder\SentimentAnalysisOfRestaurantsData\TrainDataSet\IntegratedCons.txt"
posFileVar="C:\Users\Niran0303\Google Drive\Hackrpi\New folder\SentimentAnalysisOfRestaurantsData\TrainDataSet\IntegratedPros.txt"
fileName="C:\\Users\\Niran0303\\Google Drive\\Hackrpi\\New folder\\SentimentAnalysisOfRestaurantsData\\TrainDataSet\\reviewsR.txt"
reviewData=open(fileName)
negData=open(negFileVar)
posData=open(posFileVar)
Reviews=map(lambda x:parse(x),reviewData.readlines())
negReview=map(lambda x:parse_second(x,'negative'),negData.readlines())
posReview=map(lambda x:parse_second(x,'positive'),posData.readlines())



#Reviews.extend(negReview)
#Reviews.extend(posReview)
print Reviews[:5]
all_data=[]
for (data,sent) in Reviews:
	all_data.extend(data)
print len(all_data)
dataFreq= nltk.FreqDist(all_data)
#print dataFreq
word_features= dataFreq.keys()
#print word_features


def extract_features(document):
	global word_features
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features
#print extract_features(['love', 'this', 'car'],word_features)


training_set = nltk.classify.apply_features(extract_features,Reviews)

#tainingset=["food","good"]
classifier = nltk.NaiveBayesClassifier.train(training_set)


print classifier.show_most_informative_features(32)

print classifier.classify(extract_features(['food','is','good']))
t="Save yourself the time and trouble and skip this one!"
print classifier.classify(extract_features(['after', 'that', 'they', 'complained', 'about', 'small']))
x="rude manager"
print classifier.classify(extract_features(x.split()))

print classifier._label_probdist.prob('positive')
print classifier._label_probdist.prob('negative')
print classifier.show_most_informative_features(32)


predictFile="C:\\Users\\Niran0303\\Google Drive\\Hackrpi\\restaurantReviews.csv"
predictData=open(predictFile)
outputfile="C:\\Users\\Niran0303\\Google Drive\\Hackrpi\\restaurantopReviews.csv"
outfile=open(outputfile,'w')
for x in predictData.readlines():
	d=x.split('~')
	#print d[5]
	review=classifier.classify(extract_features(d[5].split()))
	t=d[:]
	t[5]=review
	outfile.write('~'.join(t))
	#print '~'.join(t)
	
	
	
	
outfile.close()
reviewData.close()
predictData.close()