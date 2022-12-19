import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine

#conecta con la base de datos existente en docker
class sender:
    def __init__(self,file):
        

        df = pd.read_csv(file, sep="|", decimal=",")
        engine= create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")
        print("Escriba un nombre para la tabla: ")
        nombre = input()
        df.to_sql(nombre ,engine)


