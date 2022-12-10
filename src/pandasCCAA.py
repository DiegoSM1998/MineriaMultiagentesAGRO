# 4ª. En las comunidades donde es rica la ingesta de verduras y 
# frutas hubo una menor tasa de mortalidad por covid. (David)

import pandas as pd

df = pd.read_csv("covidCCAA.csv", sep=",")

# Eliminamos las columnas innecesarias
df.drop(["OBJECTID_1","OBJECTID","CodigoProv","Texto",
        "Nombre1","Nombre2","Fecha","CCAA",
        "Altas","Shape__Area","Shape__Length",
        "Recuperados","HoraActualizacion","AltasDomiciliarias","Infectados",
        "Hospitalizados","EnDomicilio","Ingresos","UCI","CasosConfirmadosEnSanitarios",
        "CasosPosibles","Fuente","NuevoCasos","Notas","GlobalID","CreationDate","Creator",
        "EditDate","Editor","TipoFuente","Habitantes"], inplace=True, axis=1)


# Rellenamos los valores numericos NaN con cero y las filas con atributos cualitativos vacios
# las eliminamos directamente
df.dropna(subset=['FechaNormalizada','NombreCCAA'])
df['CasosConfirmados'] = df['CasosConfirmados'].fillna(0)
df['Fallecidos'] = df['Fallecidos'].fillna(0)
df['FechaNormalizada'] = pd.to_datetime(df['FechaNormalizada']).dt.date
df.insert(1, 'Dia', pd.to_datetime(df['FechaNormalizada']).dt.day)
df.insert(2, 'Mes', pd.to_datetime(df['FechaNormalizada']).dt.month)
df.insert(3, 'Year', pd.to_datetime(df['FechaNormalizada']).dt.year)

# Agrupamos por CCAA y por mes, de esta manera tenemos las base de datos con todos
# los casos y fallecidos en cada Comunidad mensualmente
df.rename(columns = {'NombreCCAA':'CCAA'}, inplace = True)
df = df.groupby(['CCAA','Mes'], as_index=False).agg({'CasosConfirmados':'sum', 'Fallecidos':'sum', 'Year':'max'})
ccaa = df['CCAA'].drop_duplicates().tolist()
print(ccaa)

df1 = pd.read_csv("consumoAlimCCAA.txt", sep="|", decimal = ",")
df1.drop(['Unnamed: 10', 'Unnamed: 11', 'Consumo per capita','Gasto per capita',
        'Valor (miles de €)','Precio medio kg'], inplace=True, axis=1)

indexYear = df1[ df1['Año'] != 2020].index
df1.drop(indexYear , inplace=True)
df2 = df1.loc[(df1['Mes'] == 'Marzo') | (df1['Mes'] =='Abril') | (df1['Mes'] =='Mayo') | (df1['Mes'] =='Junio')]
df2.loc[df2["Mes"] == "Marzo", "Mes"] = 3
df2.loc[df2["Mes"] == "Abril", "Mes"] = 4
df2.loc[df2["Mes"] == "Mayo", "Mes"] = 5
df2.loc[df2["Mes"] == "Junio", "Mes"] = 6

# Exportacion de la base de datos procesada y limpia
df_final = pd.merge(df, df2, on="CCAA")
df_final.rename(columns = {'Mes_y':'Mes'}, inplace = True)
df_final.drop('Mes_x', inplace=True, axis=1)
print(df.dtypes)
df.to_csv('prueba.csv', index=False)
df2.to_csv('prueba2.csv', index=False)
df_final.to_csv('pruebaFINAL.csv', index=False)
