#!/usr/bin/python3
# -- coding: utf-8 --
'''Mostrar tablas disponibles'''

import pandas as pd
from sqlalchemy import create_engine

def chooseTable():
    engine = create_engine("postgresql://docker:docker@localhost/AGROdb")

    query = '''SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';'''

    df =pd.read_sql(query, engine)

    contador=0
    print(df)
    eleccion = input("Escoge la tabla por su indice: ")
    for val in df.values:contador+=1
    while(int(eleccion)<0 or int(eleccion)>(contador)):
        eleccion = input("Escoge un indice valido: ")
    contador=0
    tablas=[]
    for name in df.values:
        tablas.append((str(name).strip('''['']''')))
    print(str(tablas[eleccion]))
        
chooseTable()
    
#POST para eliminar data de postgres en vez de select
