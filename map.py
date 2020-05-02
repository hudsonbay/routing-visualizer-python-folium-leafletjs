# folium dependencies for the map
import folium
from folium import plugins

# dependencies from python
import os
import json

# for showing in console
from pprint import pprint

# methods to decode the json file
from json_decoding import get_routes, get_orders

# for the color of the lines
import randomcolor

# Global tooltip
tooltip = 'This is where it all starts'

# Load JSON
json_data = json.load(open('example.json'))

# parsing all the routes into objects and adding them into a list
routes_list = get_routes(json_data['routesList'])

# inserting the data from the list into the map
origin_name = ''

# Create map object
m = folium.Map(location=[routes_list[0].origin.latitude,
                         routes_list[0].origin.longitude], zoom_start=12, control_scale=True)

# Measure control
measure_control = plugins.MeasureControl(
    position='topleft', active_color='red', completed_color='red', primary_length_units='kilometers')
m.add_child(measure_control)

# Draw
""" draw = plugins.Draw(export=True)
draw.add_to(m) """


for i in routes_list:
    lat_origin = i.origin.latitude
    lon_origin = i.origin.longitude

    # esto es para evitar que se repita dibujar el mismo origin en el mapa
    # cada vez que se pasa por una orden. O sea, que solo se haga una vez y si se
    # repite que no se haga nada
    if i.origin.description != origin_name:
        """ folium.Marker([lat_origin, lon_origin], popup=i.origin.description,
                      tooltip=tooltip, icon=logoIcon).add_to(m) """
        origin_name = i.origin.description

    # creating coordinates and routes on the map
    stops_list = []
    origin_coordinates = [lat_origin, lon_origin]
    stops_list.append(origin_coordinates)  # first mark where the route starts

    # adding the stops coordinates to the _stops_list
    for stop in i.listaParadas:
        stop_coordinates = [stop.latitude, stop.longitude]
        stops_list.append(stop_coordinates)
        pprint(stop.deliveries_list)

    # add markers 'coordinates'
    for each in stops_list:
        m.add_child(folium.CircleMarker(location=each,
                                        fill='true',
                                        radius=6,
                                        popup='Hi',
                                        fill_color='red',
                                        color='clear',
                                        fill_opacity=1))
        """ folium.Marker(location=each, popup='Hi', icon=folium.Icon(
            icon='glyphicon-plane', prefix='glyphicon')).add_to(m) """

    # generating random colors for polygons
    route_color = randomcolor.RandomColor().generate()

    # drawing the polygons
    """ polyline = folium.PolyLine(
        locations=stops_list, weight=3, color=route_color) """

    polyline = plugins.AntPath(
        locations=stops_list, color=route_color, delay=1200).add_to(m)
    m.add_child(polyline)


# Generate map
m.save('map.html')
