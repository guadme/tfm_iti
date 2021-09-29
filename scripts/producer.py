# -*- coding: utf-8 -*-
"""

Real time logs simulator

"""

import time
import pandas as pd
from data import get_logs
from data import json_serializer
from kafka import KafkaProducer




producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         api_version=(0,11,5),
                         value_serializer=json_serializer)
print("....Starting Producer....")
logs = get_logs()


if __name__ == "__main__":
    while 1 == 1:
        for i in range(len(logs.index)):
            current_log = logs.to_dict('records')[i]
            if(not pd.isna(current_log['payload'])):
                print("....Sending message...")
                producer.send("logs-iti", current_log)
                print("***Message posted***")
                time.sleep(5)
        