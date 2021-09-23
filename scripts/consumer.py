# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:37:54 2021

@author: guill
"""

from kafka import KafkaConsumer
import json
from json import loads


#consumer = KafkaConsumer('logs-iti',bootstrap_servers = 'localhost:9092',auto_offset_reset = 'latest',enable_auto_commit = False,group_id = 'group-iti'#value_deserializer=lambda m: json.loads(m.decode('ascii')))
    
consumer = KafkaConsumer('logs-iti',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',enable_auto_commit=True)
    

    
for message in consumer:
    stud_obj = json.loads(message.value.decode('utf-8'))
    payload = stud_obj['payload']
    # Vectorize the payload by creating character n-grams
    res = modelo(payload_vec)
    print(str(stud_obj["url"]))
    
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        