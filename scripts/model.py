#!/usr/bin/env python
# coding: utf-8

# # Modeling the CSIC 2010 Dataset for TFM ITI

# # Classifiers

# ### Import libraries

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('./data/TR_traffic_dataset.csv')

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

# Concatenate the datasets
df3 = pd.concat([df2_norm, df2_anom])


# Create the TF-IDF Vectorizer
vec = TfidfVectorizer(analyzer='word',ngram_range=(1,2))


# Vectorize the payload of all the dataset
y = df3['label']
X = vec.fit_transform(df3['payload'].dropna())

#Split train & test for models
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)

"""
######################## Classifier Models #################################
#Logistic Regression
lgs = LogisticRegression()
lgs.fit(X_train, y_train)
pred = lgs.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


#Decesion Tree
dtc = tree.DecisionTreeClassifier()
dtc.fit(X_train, y_train)
pred = dtc.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


#Random Forest
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
pred = rfc.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


#Linear SVM
svm=LinearSVC(C=1)
svm.fit(X_train, y_train)
pred = svm.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
f1_score = metrics.f1_score(y_test, pred)
conf_matrix = metrics.confusion_matrix(y_test, pred)

print(accuracy, f1_score)
print(conf_matrix)


import pickle

# Save best model to file in the current working directory
pkl_filename = "pickle_svm.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(svm, file)


"""
