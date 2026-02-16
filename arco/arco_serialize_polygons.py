from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF
from shapely.geometry import Polygon
import re

try: 
    g = Graph()
    ttl_file = "C:/BACKUP/phd/[thesis]/conferences/inferencing/data/arco/rule-5-lombardia-geo.ttl"
    # g.parse("rule-6-prepare-lombardia-geo.ttl", format="turtle")
    g.parse(ttl_file, format="turtle")
except Exception as e:
    print('error')    
    print(e)    

ALOC = Namespace("https://w3id.org/arco/ontology/location/") 
GEO = Namespace("http://www.opengis.net/ont/geosparql#")
CLVAPIT = Namespace("https://w3id.org/italia/onto/CLV/")

# Helper: extract numeric suffix for ordering
def extract_index(uri):
    m = re.search(r"coordinates-(\d+)$", str(uri))
    return int(m.group(1)) if m else 0

g_poly = Graph()
for geom in set(g.subjects(predicate=ALOC.hasCoordinates)):
    if (geom, CLVAPIT.hasGeometryType, CLVAPIT.Polygon) in g:
        coords = []
        print("geom in if")
        print({geom})

        for coord in g.objects(geom, ALOC.hasCoordinates):
            idx = extract_index(coord)
            lat = g.value(coord, ALOC.lat)
            lon = g.value(coord, ALOC.long)
            if lat and lon:
                coords.append((idx, float(lon), float(lat)))

        # Sort by index
        coords.sort(key=lambda x: x[0])
        points = [(lon, lat) for _, lon, lat in coords]

        polygon = Polygon(points)
        wkt = polygon.wkt  
        g_poly.add((geom, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral)))

        # wkt = f"POLYGON(({', '.join([f'{x} {y}' for x, y in points])}))"
        print(wkt)

g_poly.serialize(destination="polygonsSerialized.ttl", format="turtle")

# for poly in g.subjects(predicate=ALOC.hasCoordinates):
#     coords = []
#     for coord in g.objects(poly, ALOC.hasCoordinates):
#         # assume coordinate nodes have x/y values
#         x = float(g.value(coord, URIRef("https://w3id.org/arco/ontology/location/x")))
#         y = float(g.value(coord, URIRef("https://w3id.org/arco/ontology/location/y")))
#         coords.append((x, y))

#     # !! You need to ensure they’re in the correct order !!
#     polygon = Polygon(coords)

#     wkt = polygon.wkt  # → "POLYGON((x1 y1, x2 y2, ...))"
#     g.add((poly, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral)))

# g.serialize("yourdata_with_polygons.ttl", format="turtle")
