# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:18:39 2021

@author: guill
"""
import pandas as pd
from faker import Faker
import json
fake = Faker()

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_logs():
    return pd.read_csv("normalTrafficTraining.csv", sep = ",")

def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }