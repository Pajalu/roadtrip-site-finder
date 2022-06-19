import csv
from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.api import Api
from time import sleep
import ssl

ids = []


def convert():
    ssl._create_default_https_context = ssl._create_unverified_context

    nominatim = Nominatim()
    api = Api()

    with open('ww-german-postal-codes.csv', 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter=';')
        next(csv_file, None)  # Skip header
        for rows in csv_file:
            print("PLZ:", str(rows[1]))
            try:
                area = nominatim.query(rows[1] + ", Germany")
                if area.areaId() and area.areaId() not in ids:
                    ids.append(area.areaId())
                    # name = api.query('area/' + str(area.areaId()))
            except:
                print("Skipped PLZ:", str(str(rows[1])))

    ids.sort(reverse=True)

    with open('areaIDs_germany.csv', 'w', encoding='utf-8') as f:
        for id in ids:
            f.writelines(str(id))
            f.write("\n")


if __name__ == "__main__":
    convert()
