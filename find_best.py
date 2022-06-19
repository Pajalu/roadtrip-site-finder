from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import csv
from utils import query


def search():
    with open('lite-german-postal-codes.csv', 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=';')
        next(csv_file, None)  # Skip header
        for rows in csv_file:
            print("Searching for:", rows)
            name = str(rows[1]) + ", Germany"
            elements = query(areaName=name, elementType=['node', 'way', 'relation'], selector=['"internet_access"'])
            for e in elements:
                print(e.tag('name'))
            print("_")
