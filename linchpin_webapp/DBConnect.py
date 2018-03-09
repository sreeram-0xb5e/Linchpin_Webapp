from pymongo import MongoClient
import csv


def fetch_data_to_csv(usr):
    client = MongoClient()
    db = client.washi

    if (usr == all):
        data_python = db.history.find()
    else:
        data_python = db.history.find({'id': usr})

    with open('data/raw.csv','w') as f:
        f.write("id,date,url,time")
        f.write('\n')
        for data in data_python:
            f.write(data['id'])
            f.write(',')
            f.write(data['date'])
            f.write(',')
            f.write(data['url'])
            f.write(',')
            f.write(data['time'])
            f.write(',')
            f.write('\n')
    return 1
