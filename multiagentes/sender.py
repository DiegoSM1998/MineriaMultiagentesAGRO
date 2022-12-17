import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data.txt', sep="|",decimal = "," )
##> {dialect}+{driver}://{user}:{password}@{host}:{port}/{database}
engine = create_engine('postgresql://postgres:mypassword@host.docker.internal:5432/postgres')

df.to_sql("table_name4", engine)
