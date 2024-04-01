# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:20:25 2023

@author: DINAGUASSP
"""
import openpyxl
import pandas as pd

fl='C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/00_ProcesadosFEWS/Series_Pp_Interpoladas_y_Observadas_FEWS.xlsx'
wb=openpyxl.load_workbook(fl)
s=wb.sheetnames

ls=[]
for i in range(len(s)):
    v=pd.read_excel(fl,sheet_name=s[i],skiprows=(0,1,3,4),usecols=(0,1,2),index_col=(0))
    ls.append(v)

for i in range(len(ls)):
    ls[i].plot()
    ls[i].plot(x= ls[i].columns[0],y=ls[i].columns[1],style='o')
    



   
    

