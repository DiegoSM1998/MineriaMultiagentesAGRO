import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine
import pandera as pa
from pandera import Column, Check
#conecta con la base de datos existente en docker

engine = create_engine("postgresql://docker:docker@localhost/AGROdb")

query = '''SELECT * FROM "Data1.Ampli.processed"'''
df =pd.read_sql(query, engine)

#Año|Mes|CCAA|Producto||Volumen (miles de kg)|Valor (miles de €)|Precio medio kg|Penetración (%)|Consumo per capita|Gasto per capita||

meses = ["Enero", "Febrero", "Marzo", "Abril" , "Mayo" , "Junio", "Julio",
         "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
#ccaa=["Total Nacioal", "Andalucía", "Aragón", "Asturias", "Baleares",
#      "Canarias", "Cantabria", "Castilla La Mancha", "Castilla León",
#      "Cataluña", "Extremadura", "Galicia", "La Rioja", "Madrid",
#      "Murcia", "Navarra", "País Vasco", "Valencia"]
try:
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
except Exception as ex:
    print(ex)
