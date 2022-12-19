import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
import csv

#conecta con la base de datos existente en docker

engine = create_engine("postgresql://docker:docker@localhost/AGROdb")

query = '''SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';'''

df =pd(query, engine)

print(str(df))






