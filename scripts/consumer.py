# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:37:54 2021

@author: guill
"""

from kafka import KafkaConsumer

consumer = KafkaConsumer('logs-iti',bootstrap_servers='172.19.0.6:9092',auto_offset_reset='earliest',enable_auto_commit=True)
