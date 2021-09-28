# -*- coding: utf-8 -*-
"""

Necessary functions definition

"""
import pandas as pd
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_logs():
    return pd.read_csv("./data/PD_traffic_dataset.csv", sep = ",", skip_blank_lines =True)
