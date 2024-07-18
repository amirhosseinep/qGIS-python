'''
This script bulk import csv files containing polygone, points, and linestring geometries into QGIS
'''
import os
from qgis.core import QgsVectorLayer, QgsProject

csv_directory = '/home/aesmaeilpour/Downloads/qgis sample/msarfiletemp'
print("-------------------------")
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        
        # Define the layer name based on the file name
        layer_name = os.path.splitext(filename)[0]

        with open(file_path, 'r') as file:
            header = file.readline().strip().split(';')
        
        # Construct the URI dynamically > The hardcoded values are the same as the default values in the qGIS GUI
        uri_polyg = f'file:///{file_path}?type=csv&delimiter=;&maxFields=10000&detectTypes=yes&wktField=POLYGON&crs=EPSG:4326&spatialIndex=no&subsetIndex=no&watchFile=no'
        uri_points = f'file:///{file_path}?type=csv&delimiter=;&maxFields=10000&detectTypes=yes&wktField=Point&crs=EPSG:4326&spatialIndex=no&subsetIndex=no&watchFile=no'
        uri_linestring = f'file:///{file_path}?type=csv&delimiter=;&maxFields=10000&detectTypes=yes&wktField=LINE&crs=EPSG:4326&spatialIndex=no&subsetIndex=no&watchFile=no'
        # Load the CSV file as a vector layer using the 'delimitedtext' provider
        layer_polyg = QgsVectorLayer(uri_polyg, layer_name, 'delimitedtext')
        layer_points = QgsVectorLayer(uri_points, layer_name, 'delimitedtext')
        layer_linestring = QgsVectorLayer(uri_linestring, layer_name, 'delimitedtext')
        
        # Check if the layer is valid
        if layer_polyg.isValid():
            QgsProject.instance().addMapLayer(layer_polyg)
            print(f'Loaded layer: {filename}')
        
        if layer_points.isValid():
            QgsProject.instance().addMapLayer(layer_points)
            print(f'Loaded layer: {filename}')
        
        if layer_linestring.isValid():
            QgsProject.instance().addMapLayer(layer_linestring)
            print(f'Loaded layer: {filename}')