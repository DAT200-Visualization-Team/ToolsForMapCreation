import geojson

with open('oppdelt_roads.geojson') as f:
    data = geojson.load(f)
    features = data['features']

i = 0
for road in features:
    road['properties']['osm_id'] = i
    i += 1

with open('output.geojson') as f:
    data_intersection = geojson.load(f)
    features_intersection = data_intersection['features']

j = 0
for intersection in features_intersection:
    intersection['intersection_id'] = j
    j += 1
    long = intersection['geometry']['coordinates'][0]
    lat = intersection['geometry']['coordinates'][1]
    for road in features:
        road_long_start = road['geometry']['coordinates'][0][0]
        road_lat_start = road['geometry']['coordinates'][0][1]
        road_long_end = road['geometry']['coordinates'][-1][0]
        road_lat_end = road['geometry']['coordinates'][-1][1]
        if road_long_start == long and road_lat_start == lat:
            road['start_node'] = intersection['intersection_id']
            continue
        if road_long_end == long and road_lat_end == lat:
            road['end_node'] = intersection['intersection_id']

dump = geojson.dumps(data)
output = open('output_roads.geojson', 'w')
output.write(dump)
output.close()

dump = geojson.dumps(data_intersection)
output = open('output_intersection_with_id.geojson', 'w')
output.write(dump)
output.close()

print("complete")
