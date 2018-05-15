# -*- coding: utf-8 -*-
#geopandas, (spróbować w tym mapy)
#geopy 
# fiona lub [szejpel]
"""
Created on Sun May  6 19:12:47 2018

@author: Urszula
"""

from mpl_toolkits.basemap import Basemap

lat_min, lat_max = 53.8, 54.8
lon_min, lon_max = 18.0, 19.0

m = Basemap(resolution = 'i', projection = 'cyl', llcrnrlat = lat_min, urcrnrlat = lat_max, llcrnrlon = lon_min, urcrnrlon = lon_max)
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents()
m.drawmapboundary()