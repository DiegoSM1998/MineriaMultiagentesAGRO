import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine




##> {dialect}+{driver}://{user}:{password}@{host}:{port}/{database}
engine = create_engine('postgresql://postgres:mypassword@host.docker.internal:5432/postgres')
query = "SELECT * FROM tabla_consumo_raw;"
df = pd.read_sql(query, engine)

df.drop(df.columns[[ 11, 12]], axis=1, inplace = True)

df.dropna(inplace = True)

df = df[(df['Precio medio kg'] != 0)]

df.to_sql("tabla_consumo_transformada", engine)
