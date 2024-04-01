# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:00:35 2023

@author: DINAGUASSP
"""
import os
import pandas as pd 
import datetime as dt

path='C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/02_Dinagua/00_SeriesQ/'

dicc={'Fray Marcos': ['Fray Marcos','44.0','Q.obs'],
      'Paso Pache (R.5 Nueva)': ['Paso Pache (Ruta 5 Nueva)','59.1','Q.obs'],
      'Paso Roldán': ['Paso Roldán','117.0','Q.obs'], 
      'Paso de los Troncos': ['Paso de los Troncos','119.0','Q.obs']
      }

ls=[x[0] for x in os.walk(path)]

ls1=ls[1:]
ls2=[]

g=pd.DataFrame(data=(['Location Names',''],['Location Ids',''],['Time','']))

for i in range(len(ls1)):
    name=path+ls1[i].split("/")[-1]+'_proc_v0'
    if not os.path.exists(name):
        os.makedirs(name)
        ls2.append(str(name))
    for j in os.listdir(ls1[i]):
        v = pd.read_excel(os.path.join(ls1[i],j),sheet_name='Sheet0',usecols=[0,1],skiprows=1,header=None,parse_dates=(True))
        v[0]=pd.to_datetime(v[0],dayfirst=True)
        f = pd.read_excel(os.path.join(ls1[i],j),sheet_name='Datos consultados',usecols=[0,1],header=None)
        v = v.applymap(lambda x: x.replace(",", ".") if isinstance(x, str) else x)
        if f[1][0] in dicc:
            g[1][0] = dicc[f[1][0]][0]
            g[1][1] = dicc[f[1][0]][1]
            g[1][2] = dicc[f[1][0]][2]
        g.append(v).to_csv(os.path.join(ls2[i], j.split('.xls')[0]+'.csv'),index=None,header=None)
        