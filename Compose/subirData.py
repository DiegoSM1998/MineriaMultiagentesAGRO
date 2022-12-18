import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

#conecta con la base de datos existente en docker
df = pd.read_csv("Dataset1.V2_2013-20.txt", sep="|", decimal=",")
engine= create_engine("postgresql://docker:docker@localhost/AGROdb")
df.to_sql("Data1.Ampli.raw",engine)


