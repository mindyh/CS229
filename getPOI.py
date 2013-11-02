import json
from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDmGzgPcr4hJpgj-KtjF1M7jroVlPMjHCw'

google_places = GooglePlaces(YOUR_API_KEY)


# location can be the address or a dict of lat/long
def GetPOI(output_file, location="", lat_lng=None):
    # You may prefer to use the text_search API, instead.
    query_result = google_places.nearby_search(
        location=location,
        lat_lng=lat_lng,
        radius=20000)

    poi = {}

    f1 = open(output_file, 'w+')
    for place in query_result.places:
        # Returned places from a query are place summaries.
        poi["name"] = place.name
        poi["lat_lng"] = place.geo_location
        poi["types"] = place.types
        json.dump(poi, f1, indent=3, separators=(',', ': '))
        print >>f1, '\n'

GetPOI("output.txt", location="Cerritos")
