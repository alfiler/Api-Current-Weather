## DECLARACION DE IMPORTS - Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import os
from datetime import datetime
import glob
import sys
from apikey_vs import *

##DECLARACION DE VARIABLES - Variables
api_key = str(apikey()) #Insert you Api weather https://openweathermap.org/api

lat=[33.25,66.32,64.76,0.62,-32.09,0.50,47.77,-37.85,30.38,6.45]
lon=[-70.71,-70.95,27.52,-9.38,47.90,-48.31,-75.59,-64.08,30.37,-61.73]
resp_clima= pd.DataFrame()
today=datetime.now().date()
files_list = []


## FUNCIONES - Functions

def directorio_completo(directorio):
    

    path = 'C:/Users/aleja/Documents/Python Scripts'

    full = os.path.join(path,directorio)
    
    return full

## RECORRIDO DE LISTAS DE LATITUDES Y LONGITUDES - Array Lat / Lon cycle


for lati, long in zip(lat,lon):
    url_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+str(lati)+'&lon='+str(long)+'&appid='+api_key+'&units=metric&lang=sp&temp=celcius')
    clima_json= url_weather.json()
    df_weather_status = pd.json_normalize(clima_json)
    df_weather = pd.json_normalize(clima_json,"weather")
    df_weather_status[['main','description']] = df_weather[['main','description']]
    df_weather_status[['date']]=today
    df_total = pd.DataFrame(df_weather_status)
    df_resume =df_total.drop(columns='weather')
    resp_clima = pd.concat([resp_clima,df_resume])
resp_clima

## INICIO DE GUARDADO DE ARCHIVO CSV HISTORICO - Makin .CSV file for each day Historic



full = directorio_completo('historico')

if os.path.exists(full):
    print('Carpeta Historico existe')
else:
    os.mkdir(full)

to_csv = resp_clima.to_csv('Historico/Clima_'+str(today)+'.csv',sep=',')

## APERTURA DE TODOS LOS ARCHIVOS HISTORICOS - Open All Historic .CSV files

all_files = glob.glob('Historico/clima*.csv')
len(all_files)

## UNIFICACION DE TODOS LOS ARCHIVOS HISTORICOS - Unify Historic Files

for i in all_files:
    file = pd.read_csv(i)
    files_list.append(file)

df_total = pd.concat(files_list, ignore_index=True)


## INICIO DE GUARDADO DE ARCHIVO CSV UNIFICADO - Makin :CSV File

full = directorio_completo('Total')

if os.path.exists(full):
    print('Carpeta Total existe')
else:
    os.mkdir(full)
to_csv = df_total.to_csv('Total/TotalFechas.csv',sep=',')
