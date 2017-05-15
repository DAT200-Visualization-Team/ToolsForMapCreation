import geojson

with open('oppdelt_intersections.geojson') as f:
    data = geojson.load(f)
    features = data['features']

for intersection in features:
    osm_id = intersection['properties']['osm_id']
    intersection['properties'] = [osm_id]
    long = intersection['geometry']['coordinates'][0]
    lat = intersection['geometry']['coordinates'][1]
    for other_intersection in features[1:]:
        if not isinstance(other_intersection['properties'], list):
            other_long = other_intersection['geometry']['coordinates'][0]
            other_lat = other_intersection['geometry']['coordinates'][1]
            if long == other_long and lat == other_lat:
                intersection['properties'].append(other_intersection['properties']['osm_id'])
                features.remove(other_intersection)

dump = geojson.dumps(data)
output = open('output.geojson', 'w')
output.write(dump)
output.close()

print("complete")
