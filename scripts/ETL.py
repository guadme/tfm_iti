# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:35:08 2021

@author: guill
"""
import json
from consumer import consumer
from model import vec



import pickle
pickle_filename = "pickle_svm.pkl"
    
with open(pickle_filename, "rb") as file:
    pickle_model = pickle.load(file)


from elasticsearch import Elasticsearch
import requests

es = Elasticsearch('http://elasticsearch:9200')
requests.put('http://elasticsearch:9200/logs-iti')

for i in range(size):
    requests.post('http://elasticsearch:9200/logs-clean/doc/',json=document[str(i)])

for message in consumer:
    obj = json.loads(message.value.decode('utf-8'))
    payload = [obj['payload']]
    
    res = vec.transform(payload) #vectorize the payload
    
    prediction = int(pickle_model.predict(res)) #call the model
    print(prediction)
    
    obj["prediction"] = prediction #add the prediction to the dictionary
    
    json_doc = json.dumps(obj, indent = 4)#Convert dict to json
    
    requests.post('http://elasticsearch:9200/logs-iti/doc/',json=json_doc) #post into elasticsearch
