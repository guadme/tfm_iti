# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:23:50 2021

@author: guill
"""

import time
import json
from data import get_logs
from data import json_serializer
from kafka import KafkaProducer




producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=json_serializer)

#registered_user = get_registered_user()
logs = get_logs()


if __name__ == "__main__":
    while 1 == 1:
        for i in range(len(logs.index)):
            current_log = logs.to_dict('records')[i]
            print(current_log)
            producer.send("logs-iti", current_log)
            time.sleep(5)
        