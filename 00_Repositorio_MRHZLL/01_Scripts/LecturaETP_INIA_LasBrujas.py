# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:10:46 2023

@author: DINAGUASSP
"""

import openpyxl
import pandas as pd

fl='C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/03_INIA/INIA_LasBrujas_SerieHistorica.xlsx'
wb=openpyxl.load_workbook(fl)
s=wb.sheetnames

ls=[]
for i in range(len(s)):
    v=pd.read_excel(fl,sheet_name=s[i],skiprows=(0,1),usecols=(0,1),index_col=(0),header=0,names=["Fecha","ETP"])
    v.sort_index(ascending=True,inplace=True)
    ls.append(v)
    
ls[0].to_excel('C:/Users/DINAGUASSP/Documents/00_MRHZLL/00_Datos/03_INIA/INIA_LasBrujas_FormatoFews_py.xlsx')


