#!/usr/bin/python3
# -- coding: utf-8 --
'''Scraper Consultas'''

import pandas as pd
import pandera as pa
from sqlalchemy import create_engine
from pandera import Column, Check
#conecta con la base de datos existente en docker

engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

query = '''SELECT * FROM "Data1.Ampli.processed"'''
df =pd.read_sql(query, engine)

meses = ['Enero', 'Febrero', 'Marzo', 'Abril' , 'Mayo' , 'Junio', 'Julio',
         'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
#ccaa=["Total Nacioal", "Andalucía", "Aragón", "Asturias", "Baleares",
#      "Canarias", "Cantabria", "Castilla La Mancha", "Castilla León",
#      "Cataluña", "Extremadura", "Galicia", "La Rioja", "Madrid",
#      "Murcia", "Navarra", "País Vasco", "Valencia"]

schema = pa.DataFrameSchema(
    {
        "Año": Column(int, Check.greater_than(2000)),
        "Mes": Column(str, Check.isin(meses)),
        "CCAA": Column(str),
        "Producto": Column(str),
        "Volumen (miles de kg)": Column(float, Check.greater_than(0)),
        "Valor (miles de €)": Column(float, Check.greater_than(0)),
        "Precio medio kg": Column(float, Check.greater_than(0)),
        "Penetración (%)": Column(float, Check.greater_than(0)),
        "Consumo per capita": Column(float, Check.greater_than(0.0)),
        "Gasto per capita": Column(float, Check.greater_than(0.0))
    }
)

schema.validate(df)
