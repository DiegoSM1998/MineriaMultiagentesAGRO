#!/usr/bin/python3
# -- coding: utf-8 --
'''Limpieza pandas postgresql'''

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

query = '''SELECT * FROM "Data1.Ampli.raw"'''
df =pd.read_sql(query, engine)

df.drop(df.columns[[ 11, 12]], axis=1, inplace = True)

df.dropna(inplace = True)

df = df[(df['Precio medio kg'] != 0)]

df.to_sql("Data1.Ampli.processed",engine)
