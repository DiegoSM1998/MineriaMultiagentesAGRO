import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

engine= create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

files = os.listdir('data')

for file in files:
    if file.endswith('.txt'):
        with open(os.path.join('data', file), 'r') as f:
            df = pd.read_csv(f,sep="|", decimal=",")
            print(df)
            df.to_sql(file + ".raw",engine)



