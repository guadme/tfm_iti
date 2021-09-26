# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:18:39 2021

@author: guill
"""
import pandas as pd
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_logs():
    return pd.read_csv("./data/PD_traffic_dataset.csv", sep = ",", skip_blank_lines =True)
