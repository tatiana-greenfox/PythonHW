from pymongo import MongoClient
from datetime import datetime
import csv
import re

def read_data(path):
    with open(path, encoding='utf-8') as csv_file:
        line = csv.reader(csv_file, delimiter=",")
        data_list = list(line)
        header = data_list.pop(0)

        return data_list

def return_collection(db_name, collection_name): 
    client = MongoClient()
    db = client[db_name]
    collection = db[collection_name]
    
    return collection

def create_documents(db_name, collection_name, data):
    collection = return_collection(db_name, collection_name)

    data_list = read_data(data)
    
    for value in data_list:
        
        document = {
            'name': value[0],
            'cost': int(value[1]),
            'place': value[2],
            'date': datetime.strptime(f'{value[3]}.2020', '%d.%m.%Y')
        }

        collection.insert_one(document)

    return collection

def find_cheapest(db_name, collection_name): # отсортировать билеты из базы по возрастанию цены
    collection = return_collection(db_name, collection_name)

    artists = collection.find().sort('cost', 1)

    for artist in artists:
        print(artist)

def find_by_name(artist_name, db_name, collection_name): # найти билеты по исполнителю, где имя исполнителя может быть задано не полностью, и вернуть их по возрастанию цены.
    collection = return_collection(db_name, collection_name)

    pattern_name = re.compile(artist_name, re.IGNORECASE)
    
    artists = collection.find({'name': pattern_name}).sort('cost', 1)

    for artist in artists:
        print(artist)

def find_date(db_name, collection_name, date_first, date_last): # сортировка по дате мероприятия
    collection = return_collection(db_name, collection_name)
    df = datetime.strptime(date_first, '%d.%m.%Y')
    dl = datetime.strptime(date_last, '%d.%m.%Y')

    artists = collection.find({'date': {'$lte': dl}}).sort('date', 1)

    for artist in artists:
        print(artist)


if __name__ == "__main__":
    # create_documents('tickets_manager_4', 'concerts_information', 'artists.csv')
    find_by_name('S', 'tickets_manager_4', 'concerts_information')
    # find_cheapest('tickets_manager_4', 'concerts_information')
    # find_date('tickets_manager_4', 'concerts_information')