# -*- coding: utf-8 -*-
"""

Read messages from kafka topic, process them, load them into ELK

"""
import json
from datetime import datetime
from consumer import consumer
from model import vec
import pickle
import warnings
from elasticsearch import Elasticsearch
import requests

#Ignore warnings

warnings.filterwarnings("ignore")

#Load trained model

pickle_filename = "pickle_dtc.pkl"
with open(pickle_filename, "rb") as file: 
    pickle_model = pickle.load(file)

#Connect to ELK

es = Elasticsearch('http://elasticsearch:9200')
requests.put('http://elasticsearch:9200/logs-iti')

print("Starting...")
print("Waiting for messages")
for message in consumer:
    
    print("New message:")
    
    obj = json.loads(message.value.decode('utf-8'))
    payload = [obj['payload']]
    
    res = vec.transform(payload) #vectorize the payload
    
    prediction = int(pickle_model.predict(res)) #call the model
    print("Prediction = " + str(prediction))
    
    obj["prediction"] = prediction #add the prediction to the dictionary
    
    date= str(datetime.now().date())
    time= str(datetime.now().time())
    obj["timestamp"] = date+'T'+time #add timestamp to the dictionary for visualization purposes
        
    requests.post('http://elasticsearch:9200/logs-iti/doc/',json=obj) #post into elasticsearch
        
    print("Message successfully processed and loaded to ELK")