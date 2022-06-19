from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.api import Api
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass

nominatim = Nominatim()
api = Api()
overpass = Overpass()


def query(areaId=None, areaName=None, elementType=None, selector=None):
    if areaId:
        print("ID:", areaId, "-> Name:", areaName)
    elif areaName:
        nm_query = nominatim.query(areaName)
        areaId = nm_query.areaId()
        print("Name:", areaName, "-> ID:", areaId)
    else:
        raise ValueError("No area information! Please provide areaId or areName.")

    new_query = overpassQueryBuilder(area=areaId, elementType=elementType, selector=selector, includeGeometry=True)
    result = overpass.query(new_query)
    print(result.countElements(), "elements found:",
          result.countNodes(), "nodes,",
          result.countWays(), "ways,",
          result.countRelations(), "relations")

    return result.elements()
