# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:47:58 2023

@author: DINAGUASSP
"""
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

# file='C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/MetIn_2000_2015.nc'
# v=nc.Dataset(file)

fl1='C:/Repositorios/FEWS-Uruguay/trunk/FEWS-UY/Uruguay/Export/NC/20211231.nc'
# n=nc.Dataset(fl1)
# n.variables

v=nc.Dataset(fl1)
# ls=list(v.variables.keys())

for i in range(len(ls)):
    x=ls[i]
    globals()[x] = v.variables[str(ls[i])][:] #globals para convertir de str a una variable de py
    # da como resultado las variables: time, lat, lon, precip, pet, temp, spatial_ref

map = Basemap(projection='merc',llcrnrlon=-58.,llcrnrlat=-35.,urcrnrlon=-54.,urcrnrlat=-33.,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full
map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)

# parallels = np.arange(30,50,5.) # make latitude lines ever 5 degrees from 30N-50N
# meridians = np.arange(-95,-70,5.) # make longitude lines every 5 degrees from 95W to 70W
# map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

lons,lats= np.meshgrid(lon,lat)
x,y = map(lons,lats)

pp = map.contourf(x,y,precip[3392,:,:])
cb = map.colorbar(pp,"bottom", size="5%", pad="2%")
plt.title('Precipitación')
cb.set_label('Precipitación [mm]')

plt.savefig(r'C:\Users\vanessa.erasun\Documents\00_Trabajo\04_Scripts\01_Netcdf\netcdf_pp.jpeg',dpi=300)
plt.show()
