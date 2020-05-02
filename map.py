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
