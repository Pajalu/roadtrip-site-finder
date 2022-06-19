import os
import ssl
from OSMPythonTools.api import Api
from utils import query


def search(area=None, selectors=None, key=None):
    elements1 = query(area, selectors, key)

    with open('found_elements.csv', 'w', encoding='utf-8') as f:
        for e in elements1:
            elementName = e.tag('name')
            if not elementName:
                elementName = "Unknown"
            print(elementName)
            f.writelines(elementName)
            f.write("\n")

