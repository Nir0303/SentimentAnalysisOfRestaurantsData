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
#Predict decision tree results
dt.predict(M[:3653,:])