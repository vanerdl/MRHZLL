#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:30:44 2022

@author: vanerdl
"""

# =============================================================================
# Datos de Caudales -  Dinagua para Indice de Caudales
# =============================================================================
import pandas as pd
from os import listdir
from os.path import isfile, join

# mypath= '/home/dinagua/Escritorio/Proyectos/Diangua/20220808-20220822_Datos/'
# mypath='E:/Datos_PP_PasoPache/Dinagua/20220808-20220822_Datos/'
mypath='E:/Datos_PP_PasoPache/Dinagua/20220823-20220906_Datos/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
mypath_new='E:/Datos_PP_PasoPache/Dinagua/20220823-20220906_Datos_procesados/'

ls=[]
for file in onlyfiles: 
    v=pd.read_csv(mypath+str(file),header=None)
    v[0][3:]=pd.to_datetime(v[0][3:])
    ls.append(v)
    
ls1=[] 
for i in range(len(ls)):
    n=pd.DataFrame(columns= ('Time', 'Q'))
    n['Time']=ls[i][0][3:]
    n['Q']=pd.to_numeric(ls[i][2][3:])
    n['Time']=pd.to_datetime(n['Time'])
    n.set_index(n['Time'],inplace=True)
    n=n.drop(columns='Time',axis=1)
    n=n.resample('D').mean()
    n['Id']=ls[i][1][1]
    n['Index']=n.index
    ls1.append(n)
    ls1[i].to_csv(mypath_new+str(ls[i][1][1])+'_'+str(ls[i][1][0])+'.csv', index=False,header=False,date_format='%d/%m/%Y',columns=['Id','Index','Q'])


# =============================================================================
# Datos de precipitación - Inumet 
# =============================================================================

ls2=[]
mypath='/home/dinagua/Escritorio/Proyectos/INUMET/Datos_PP_PasoPache/02_Convencionales/'
mypath_new='/home/dinagua/Escritorio/Proyectos/INUMET/Datos_PP_PasoPache/02_Convencionales_proc/'
def serieInumet(mypath,mypath_new):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles: 
        v=pd.read_csv(mypath+str(file),header=None)
        v[0][3:]=pd.to_datetime(v[0][3:])
        v[0][3:]=v[0][3:].dt.round('min')
        ls2.append(v)
        
    for i in range(len(ls2)):
        ls2[i].to_csv(mypath_new+str(ls2[i][1][0])+'.csv', index=False,header=None)

serieInumet(mypath, mypath_new)









