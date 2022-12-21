#!/usr/bin/python3
# -- coding: utf-8 --
'''Limpieza pandas postgresql'''

import pandas as pd
from sqlalchemy import create_engine

def chooseTable():
    engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

    query = '''SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';'''

    df =pd.read_sql(query, engine)

    contador=0
    print(df)
    eleccion = input("Escoge la tabla por su indice: ")
    for val in df.values:contador+=1
    while(int(eleccion)<0 or int(eleccion)>(contador-1)):
        eleccion = input("Escoge un indice valido: ")
    contador=0
    tablas=[]
    for name in df.values:
        tablas.append(str(name).strip('''['']'''))
    elegida=str(tablas[int(eleccion)])
    print("Tabla seleccionada: "+elegida)
    return elegida

engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")
tabla = chooseTable()
query = '''SELECT * FROM "'''+tabla+'''"'''
df =pd.read_sql(query, engine)

df.drop(df.columns[[ -1,-2]], axis=1, inplace = True)

df.dropna(inplace = True)

df = df[(df['Precio medio kg'] != 0)]

df.to_sql(str(tabla).strip('''.raw''')+".processed",engine)
