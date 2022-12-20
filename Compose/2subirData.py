import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

#conecta con la base de datos existente en docker
dirfichero=input("Escriba el fichero que desea subir a la base de datos: ")
df = pd.read_csv(dirfichero, sep="|", decimal=",")
engine= create_engine("postgresql://docker:docker@localhost/AGROdb")
df.to_sql("Data1.raw",engine)


