# TFM ITI


## Installation

Follow the steps to set up the enviroment.

1- Clone git repository (https://github.com/guadme/tfm_iti.git).

```sh
git clone https://github.com/guadme/tfm_iti.git
```

2- Run docker containers

```sh
docker-compose up -d
```

3- Create kafka topic called "logs-iti"

```sh
docker exec -it {kafkaID} /bin/sh

$ cd opt/bitnami/kafka/bin
$ kafka-topics.sh -- create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic logs-iti
```

4 - Check if the topic has been created.

```sh
$ kafka-topics.sh --listr --zookeeper zookeeper:2181
```

5- Create data directory in jupyter container where scripts will be executed.

```sh
docker exec -it {jupyterID} /bin/sh

$ cd work
$ mkdir data
```

6- Copy scripts and data from local repository to jupyter container.

```sh
cd scripts

docker cp "consumer.py" {juoyterID}:"home/jovyan/work"
docker cp "data.py" {juoyterID}:"home/jovyan/work"
docker cp "ETL.py" {juoyterID}:"home/jovyan/work"
docker cp "model.py" {juoyterID}:"home/jovyan/work"
docker cp "producer.py" {juoyterID}:"home/jovyan/work"
docker cp "pickle_svm.pkl" {juoyterID}:"home/jovyan/work"

cd data
docker cp "PD_traffic_dataset.csv" {jupyterID}:"home/jovyan/work/data"
docker cp "TR_traffic_dataset.csv" {jupyterID}:"home/jovyan/work/data"
```

7- Install necessary python modules

```sh
docker exec -it {jupyterID} /bin/sh
$ cd work
$ python requirements.txt
```

8- Run python scripts

```sh
docker exec -it {jupyterID} /bin/sh
$ cd work
$ python data.py
$ python model.py
$ python consumer.py
$ python ETL.py

//In another window

docker exec -it {jupyterID} /bin/sh
$ python producer.py
```