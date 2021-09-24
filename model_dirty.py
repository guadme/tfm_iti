#!/usr/bin/env python
# coding: utf-8

# # Modeling the CSIC 2010 Dataset for TFM ITI

# # Classifiers

# ### Import libraries

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn import metrics


df = pd.read_csv('TR_traffic_dataset.csv')

# Remove columns that contain the same values
df = df.drop(['userAgent', 'pragma', 'cacheControl', 'acceptEncoding', 'acceptCharset', 'acceptLanguage'], 1)
df = df.drop(['connection', 'cookie', 'accept', 'protocol'], 1)

# Keep only the port because everything else is localhost
df['port'] = df['host'].str.split(':', expand=True)[1]
df = df.drop(['host'], 1)
df.head()

# Split the dataset in two to avoid mixed indices
df_anom = df[df['label']=='anom']
df_norm = df[df['label']=='norm']

df2_anom = df_anom[['index', 'payload', 'label']]
df2_anom = df2_anom.dropna()
df2_anom['label'] = 1


df2_norm = df_norm[['index', 'payload', 'label']]
df2_norm = df2_norm.dropna()
df2_norm['label'] = 0
"""
df3_anom = df2_anom[['payload','label']].groupby(df2_anom['index']).agg(lambda x: ' '.join(set(x)))
df3_anom["payload"] = df3_anom['payload'].apply(lambda x: x.replace("=", " "))

df3_anom['label'] = 1


df3_norm = df2_norm[['payload','label']].groupby(df2_norm['index']).agg(lambda x: ' '.join(set(x)))
df3_norm["payload"] = df3_norm['payload'].apply(lambda x: x.replace("=", " "))

df3_norm['label'] = 0
"""

df4 = pd.concat([df2_norm, df2_anom])

vec = TfidfVectorizer(analyzer='word',ngram_range=(1,2))




# Vectorize the payload of all the dataset

y = df4['label']
X = vec.fit_transform(df4['payload'].dropna())



import json
from kafkaconsumer import consumer

for message in consumer:
    stud_obj = json.loads(message.value.decode('utf-8'))
    payload = [stud_obj['payload']]
    res = vec.transform(payload)
    print(res)
    
    
    

import pickle
pickle_filename = "pickle_svm.pkl"
    
with open(pickle_filename, "rb") as file:
    pickle_model = pickle.load(file)
    
    
predition = pickle_model.predict(res) 

# In[76]:
"""

payload = [df4.loc[1]["payload"]]


# In[77]:


X = vec.transform(payload)


# In[78]:


X


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)


# In[20]:


#Logistic Regression
lgs = LogisticRegression()
lgs.fit(X_train, y_train)
pred = lgs.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


# In[ ]:


#Decesion Tree
dtc = tree.DecisionTreeClassifier()
dtc.fit(X_train, y_train)
pred = dtc.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


# In[ ]:


#Random Forest
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
pred = rfc.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


# In[21]:


#Linear SVM
svm=LinearSVC(C=1)
svm.fit(X_train, y_train)
pred = svm.predict(X_test)



accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


# #### Save model

# In[46]:


import pickle

# Save to file in the current working directory
pkl_filename = "pickle_lgs.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(lgs, file)


# #### Load model

# In[50]:


# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
    
# Predict target values
#score = pickle_model.score(Xtest, Ytest)
#print("Test score: {0:.2f} %".format(100 * score))
#Ypredict = pickle_model.predict(Xtest)


# In[80]:


pickle_model.predict(X)


# In[ ]:
"""



