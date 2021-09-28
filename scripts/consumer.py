# -*- coding: utf-8 -*-
"""

Kafka consumer script - topic "logs-iti"

"""

from kafka import KafkaConsumer

consumer = KafkaConsumer('logs-iti',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',enable_auto_commit=True)
