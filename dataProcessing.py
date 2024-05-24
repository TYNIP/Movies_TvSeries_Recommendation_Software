import csv
from collections import defaultdict

def read_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except UnicodeDecodeError:
        with open(file_path, mode='r', encoding='latin-1') as file:
            return list(csv.DictReader(file))

def process_data(data):
    index = {
        'type': defaultdict(list),
        'director': defaultdict(list),
        'cast': defaultdict(list),
        'listed_in': defaultdict(list)
    }
    
    for entry in data:
        if entry['type']:
            index['type'][entry['type']].append(entry)
        if entry['director']:
            index['director'][entry['director']].append(entry)
        if entry['cast']:
            for actor in entry['cast'].split(', '):
                index['cast'][actor].append(entry)
        if entry['listed_in']:
            for genre in entry['listed_in'].split(', '):
                index['listed_in'][genre].append(entry)
    
    return index