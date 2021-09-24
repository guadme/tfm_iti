# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:35:08 2021

@author: guill
"""
import json
from consumer import consumer

for message in consumer:
    stud_obj = json.loads(message.value.decode('utf-8'))
    payload = stud_obj['payload']
    print(payload)
