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

es = Elasticsearch('http://localhost:9200')
requests.put('http://localhost:9200/logs-iti')

from datetime import datetime

for message in consumer:
    obj = json.loads(message.value.decode('utf-8'))
    payload = [obj['payload']]
    
    res = vec.transform(payload) #vectorize the payload
    
    prediction = int(pickle_model.predict(res)) #call the model
    print(prediction)
    
    obj["prediction"] = prediction #add the prediction to the dictionary
    
    obj["timestamp"] = str(datetime.now())
    
    json_doc = json.dumps(obj, indent = 4)#Convert dict to json
    
    requests.post('http://localhost:9200/logs-iti/doc/',json=json_doc) #post into elasticsearch
