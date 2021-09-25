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


for message in consumer:
    obj = json.loads(message.value.decode('utf-8'))
    payload = [obj['payload']]
    
    res = vec.transform(payload)
    predition = pickle_model.predict(res)
    print(predition)
