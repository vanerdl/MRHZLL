# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:18:28 2023

@author: DINAGUASSP
"""
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

# fl_fews='C:/Users/DINAGUASSP/Downloads/CaudalesCRSL-PasoPache.csv'
fl_fews='C:/Users/DINAGUASSP/Downloads/CaudalesCRSL-PasoPache_v0_7hrs.csv'
fl_rn='C:/Users/DINAGUASSP/Downloads/Caudales_observados_comparacion.csv'

dic={'23':'119.0', #Paso de los Troncos
     '41':'59.1', #Paso Pache
     '30':'117.0', #Paso Roldán 
     '36':'44.0'} #Fray Marcos

q_rn=pd.read_csv(fl_rn,index_col=0,sep=';',header=0)
q_rn.index=pd.to_datetime(q_rn.index)

q_fews=pd.read_csv(fl_fews,index_col=0,header=0)
q_fews.index=pd.to_datetime(q_fews.index)

# =============================================================================
# #Gráfica caudales observados (Dinagua vs RN)
# =============================================================================
for i in range(q_fews.shape[1]):
   n=pd.to_numeric(q_fews[q_fews.columns[i]][1:])
   n=n['2000-01-01 07:00:00':'2023-01-01 07:00:00']
   # n=n[n>0]
   n = n.replace(-999, np.nan)
   print(q_fews.columns[i])
   s=[]
   fig,ax=plt.subplots(1,1)
   for k,v in dic.items():
        if v == q_fews.columns[i]:
            print(k,q_fews.columns[i],'son la misma estación')
            # q_rn[k].plot()
            s.append(q_rn[k])
            # n.plot()
            # fig.plot(n.index,n, label='Dinagua')
            # fig.plot(s[0].index,s[0], label='RN')
            s[0].plot(label='RN')
            n.plot(label='Dinagua')
            # Agrega título y etiquetas de eje
            plt.title('Gráfico de Caudales Dinagua vs Caudales RN'+ ' Estación '+str(q_fews.columns[i]))
            plt.xlabel('Fecha')
            plt.ylabel('Caudal [m3/s]')
            
            # Agrega leyenda
            plt.legend()
            
            # Muestra gráfico
            plt.show()
            
def graficaCalor(q_fews):
    indice=pd.date_range(start=dt.datetime(2000, 1, 1), periods=23, freq='Y')
    df_mean=pd.DataFrame(index=indice,columns=q_fews.columns)
    for i in range(q_fews.shape[1]):
       n=pd.to_numeric(q_fews[q_fews.columns[i]][1:])
       print('Número de estación:',q_fews.columns[i])
       n=n['2000-01-01 07:00:00':'2023-01-01 07:00:00']
       # n=n[n>0]
       n = n.replace(-999, np.nan)
       n_nans = n.isna().sum().sum()
       n_nans_total=round(n_nans/8400,2)
       # Imprimir el número de valores NaN
       print("Número de valores NaN:", n_nans, n_nans_total)
       q_fews_y=n.resample('Y').mean()
       if q_fews.columns[i] == df_mean.columns[i]:
           df_mean[df_mean.columns[i]] = q_fews_y
           print('Listo')
    return df_mean.to_csv('C:/Users/DINAGUASSP/Downloads/CaudalesCRSL-PasoPache_v0_7hrs_media_anual_v0.csv')
           
# graficaCalor(q_fews)           

def qmed_anual_validacion_faltantesmenor25porciento(q_fews):

    lista=[]
    lista_2=[]
    for i in range(q_fews.shape[1]):
       n=pd.to_numeric(q_fews[q_fews.columns[i]][1:])
       print('Número de estación:',q_fews.columns[i])
       n=n['2000-01-01 07:00:00':'2022-12-31 07:00:00']
       n = n.replace(-999, np.nan)
       nans=n.groupby(n.index.year).apply(lambda x: round(x.isna().sum()/365,2)*100)
       nans=pd.DataFrame(nans,index=nans.index.get_level_values(0))
       q=n.groupby(n.index.year).apply(lambda x: round(x.mean(),3))
       q=pd.DataFrame(q)
       v=pd.DataFrame(columns=('q_med-'+str(q_fews.columns[i]),'nans-'+str(q_fews.columns[i])),index=q.index)
       v['nans-'+str(q_fews.columns[i])]=nans[nans.columns[0]]
       v['q_med-'+str(q_fews.columns[i])]=q[q.columns[0]]
       v['q_med_med-'+str(q_fews.columns[i])]=round(v['q_med-'+str(q_fews.columns[i])].mean(),2)
       v['q_anomalia-'+str(q_fews.columns[i])]=round(v['q_med-'+str(q_fews.columns[i])]-v['q_med_med-'+str(q_fews.columns[i])],2)
       lista.append(v)
       v=v[v['nans-'+str(q_fews.columns[i])]<25]
       v['q_med_med-'+str(q_fews.columns[i])]=round(v['q_med-'+str(q_fews.columns[i])].mean(),2)
       v['q_desv-est'+str(q_fews.columns[i])]=round(v['q_med-'+str(q_fews.columns[i])].std(),2)
       v['q_anomalia-'+str(q_fews.columns[i])]=round(v['q_med-'+str(q_fews.columns[i])]-v['q_med_med-'+str(q_fews.columns[i])],2)
       v['q_anomalia-est'+str(q_fews.columns[i])]=v['q_anomalia-'+str(q_fews.columns[i])]/v['q_desv-est'+str(q_fews.columns[i])]
       v['q_ranking-'+str(q_fews.columns[i])]=v['q_med-'+str(q_fews.columns[i])].rank(ascending=True)
       v['percentile-'+str(q_fews.columns[i])]=round(v['q_ranking-'+str(q_fews.columns[i])]/(v.shape[0]+1),2)
       s=pd.Series(index=range(v.shape[0]))
       v['categoria-'+str(q_fews.columns[i])] = s
       for index,valor in v['percentile-'+str(q_fews.columns[i])].iteritems(): 
           # print(index,valor)
            if valor>0.87:
               v['categoria-'+str(q_fews.columns[i])].at[index] = 2#"++"
            elif valor>0.72:
               v['categoria-'+str(q_fews.columns[i])].at[index] = 1#"+"
            elif valor >0.28:
               v['categoria-'+str(q_fews.columns[i])].at[index] = 0#"+/-"
            elif valor >0.13: 
               v['categoria-'+str(q_fews.columns[i])].at[index] = -1#"-"
            else: 
               v['categoria-'+str(q_fews.columns[i])].at[index] = -2#"--"
       lista_2.append(v)
       return lista,lista_2
     
qmed_anual_validacion_faltantesmenor25porciento(q_fews)

def heatmapCaudalesStaLucia(lista,lista_2):
    s=pd.DataFrame(index=lista[0].index)
    
    for i in range(len(lista_2)):
        l=lista_2[i].columns[-1]
        s[l.split("-")[1]]=lista_2[i][l]
        print (s)
    # bounds = [-2,-1,0,1,2]
    cmap=mcolors.ListedColormap(['red','orange','yellow','lime','green'])
    sns.heatmap(s.transpose(),cmap=cmap,linecolor='black',linewidths=0.1)
    # plt.savefig("figura.png")
    
    return s


heatmapCaudalesStaLucia(lista,lista_2)
    




