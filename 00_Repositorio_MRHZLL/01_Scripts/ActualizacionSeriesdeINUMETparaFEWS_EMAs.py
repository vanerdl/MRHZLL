# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:54:44 2023
@author: DINAGUASSP
"""
import pandas as pd 
from pandas.errors import EmptyDataError
import os

pathConv = 'C:/Repositorios/FEWS-Uruguay/trunk/FEWS-UY/Uruguay/Import/INUMET/EMA'
pathConv_f5 = 'C:/Users/DINAGUASSP/Downloads/EMAs_septiembre_2022_enero_2023/EMAs'
pathConv_fews = 'C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/01_Inumet/00_EMAs_proc'

ls1=[]
for i in os.listdir(pathConv):
    print(i)
    ls1.append(i)

fls1=[]
encab1=[]
for i in range(len(ls1)):
    v=pd.read_csv(pathConv+'/'+str(ls1[i]),header=None)
    v_encab=v[0:3]
    v_datos=v[3:]
    encab1.append(v_encab)
    fls1.append(v_datos)

ls1_f5=[]
for i in os.listdir(pathConv_f5):
    print(i)
    ls1_f5.append(i)

path_new=os.makedirs(pathConv_fews+'_v1')

for i in range(len(ls1)):
    print(i)
    try: 
        g=pd.read_csv(pathConv_f5+'/'+str(ls1[i]),skiprows=3,header=None)
        v=encab1[i].append(g)
        v.to_csv(pathConv_fews+'_v1'+'/'+ls1[i],header=False,index=False)     
    except EmptyDataError:
        print('No columns to parse from file')
    
    
    

