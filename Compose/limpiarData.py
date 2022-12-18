import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
import csv

#conecta con la base de datos existente en docker

engine = create_engine("postgresql://docker:docker@localhost/AGROdb")

query = '''SELECT * FROM "Data1.Ampli.raw"'''
df =pd.read_sql(query, engine)

df.drop(df.columns[[ 11, 12]], axis=1, inplace = True)

df.dropna(inplace = True)

df = df[(df['Precio medio kg'] != 0)]

df.to_sql("Data1.Ampli.processed",engine)






