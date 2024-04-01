# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:11:34 2023

@author: DINAGUASSP
"""
import netCDF4 as nc
fl_nc='C:/Repositorios/FEWS-Uruguay/trunk/FEWS-UY/Uruguay/Export/NC/20230101.nc'
v=nc.Dataset(fl_nc)
v.variables.keys()

v.
import matplotlib.pyplot as plt
import numpy as np

# Crea los datos
data = np.random.rand(10,10)

# Crea el gráfico de calor
plt.imshow(data, cmap='hot')

# Añade títulos y etiquetas
plt.title('Gráfico de Calor')
plt.xlabel('X')
plt.ylabel('Y')

# Muestra el gráfico
plt.show()
