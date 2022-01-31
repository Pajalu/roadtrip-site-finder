import os
import ssl
from OSMPythonTools.api import Api

ssl._create_default_https_context = ssl._create_unverified_context

from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
area = nominatim.query('Munich')
print("Searching in: ", area.displayName())

from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
overpass = Overpass()
query = overpassQueryBuilder(area=area.areaId(), elementType=['way', 'relation'], selector='"natural"="water"', includeGeometry=True)
result = overpass.query(query)
print(result.countElements(), " elements found")
elements = result.elements()

with open('found_elements.txt', 'w', encoding='utf-8') as f:
    for e in elements:
        elementName = e.tag('name')
        if elementName:
            corners = str(e.geometry()['coordinates'])
            print(elementName)
            f.writelines(elementName)
            f.write("\n")



