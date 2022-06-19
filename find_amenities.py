import os
import ssl
from OSMPythonTools.api import Api



from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
area = nominatim.query#('Munich')
print("Searching in: ", area.displayName())

from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
overpass = Overpass()
query = overpassQueryBuilder(area=area.areaId(), elementType=['node', 'way', 'relation'], selector='"amenity"="toilets"', includeGeometry=True)
result = overpass.query(query)
print(result.countElements(), " elements found")
elements = result.elements()

with open('found_elements.csv', 'w', encoding='utf-8') as f:
    header = "Index, Name, Lat., Long., Type"
    f.writelines(header)
    f.write("\n")

    element_no = 0

    for e in elements:
        elementName = e.tag('name')
        elementType = e.tag('elementType')
        if not elementName:
            elementName = "Unknown"

        element_coordinates = str(e.geometry()['coordinates'])
        element_coordinates = str.replace(element_coordinates, "[", "")
        element_coordinates = str.replace(element_coordinates, "]", "")

        f.writelines(str(element_no) + ", " + elementName + ", " + element_coordinates + ", " + str(elementType))
        f.write("\n")
        element_no +=1



