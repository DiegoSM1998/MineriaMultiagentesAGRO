#!/usr/bin/python3
# -- coding: utf-8 --
'''Subir data a postgresql'''

import pandas as pd
from sqlalchemy import create_engine

#conecta con la base de datos existente en docker
df = pd.read_csv("Data/Dataset1.V2_2013-20.raw", sep="|", decimal=",")
engine= create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")
df2 = pd.read_csv("Data/Dataset1.V1_2018-20.raw", sep="|", decimal=",")
df.to_sql("Data1.Ampli.raw",engine)
df2.to_sql("Data1.raw",engine)
