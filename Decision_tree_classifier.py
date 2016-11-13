import pandas as pd
import numpy as np
import os
import subprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
#read training data
df=pd.read_csv("E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\train_restaurant_data.txt",delim_whitespace=False,header='infer',sep="~")
#udf for converting classifying target column 
def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()#find unique values in Feedback column
    map_to_int = {name: n for n, name in enumerate(targets)}#creates enumerated tyoes for feedback column
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)#create new column target with 0,1 as classifying identities
    return (df_mod, targets)
#call function with target column and capture results
df2, targets = encode_target(df, "Feedback")
#convert the review column to list
features = list(df2.columns[:1])
#extract one element of df2 dataset
y = df2["Target"]
#convert features to list
X=df2[features].values.tolist()
a=[ i[0] for i in X]
#convert text data to numberic using LabelEncoder
Z=le.fit(a)
ZZ=le.transform(np.array(a).reshape(-1,1))
#Decision tree classifier training model
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(ZZ, y)

lines = open("E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\test_restaurant_data.txt","r")
list_vec=[]
for columns in (raw.strip().split("~") for raw in lines):
    list_vec.extend(columns[5].split(" "))
#convert text data to numeric using LabelEncoder
res = le.fit(list_vec)
M=le.transform(np.array(list_vec).reshape(-1,1))
#Predict decision tree results on test data
o=dt.predict(M[:3653,:])

#Write results to a file for generating graphs
#fl_write = open("E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\final_restaurant_data.txt","wb")
"""with open("E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\final_restaurant_data.txt", 'wb') as f:
        writer = csv.writer(f)
        with open("E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\test_restaurant_data.txt","r") as csvfile:
            reader = csv.reader(csvfile, delimiter='~')
            for row in reader:
                row[0] = f1.readline() # edit the 8th column
                writer.writerow(row)
                row[1] = f1.readline()
                writer.writerow(row)
                row[2] = f1.readline()
                writer.writerow(row)
                row[3] = f1.readline()
                writer.writerow(row)
                row[4] = f1.readline()
                writer.writerow(row)
                writer.writerow(dt[0])"""
        

opfile="E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\final_restaurant_data.txt"
ipfile="E:\\hackRPI\\SentimentAnalysisOfRestaurantsData-master\\test_restaurant_data.txt"
opfil=open(opfile,'w')
ipfil=open(ipfile)
cnt=0
for i in ipfil.readlines():
    x=i.split('~')
    if o[cnt]=='1':
        x[5]='negative'
    else:
        x[5]='positive'
    opfil.write('~'.join(x))
ipfil.close()
opfil.close()
lines.close()