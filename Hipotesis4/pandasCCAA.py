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

# Eliminamos Ceuta y Melilla, son ciudades autonomas y ademas no tenemos informacion de consumo sobre ellas
valores_a_eliminar = ['Ceuta', 'Melilla']
df = df.loc[~df['CCAA'].isin(valores_a_eliminar)]
ccaa = df['CCAA'].drop_duplicates().tolist()
print(ccaa)

df1 = pd.read_csv("consumoAlimCCAA.txt", sep="|", decimal = ",")
df1.drop(['Unnamed: 10', 'Unnamed: 11', 'Consumo per capita','Gasto per capita',
        'Valor (miles de €)','Precio medio kg'], inplace=True, axis=1)

# Eliminamos el total nacional para evitar errores
df1 = df1.loc[df1['CCAA'] != 'Total Nacional']

indexYear = df1[ df1['Año'] != 2020].index
df1.drop(indexYear , inplace=True)
df2 = df1.loc[(df1['Mes'] == 'Marzo') | (df1['Mes'] =='Abril') | (df1['Mes'] =='Mayo') | (df1['Mes'] =='Junio')]
df2.loc[df2["Mes"] == "Marzo", "Mes"] = 3
df2.loc[df2["Mes"] == "Abril", "Mes"] = 4
df2.loc[df2["Mes"] == "Mayo", "Mes"] = 5
df2.loc[df2["Mes"] == "Junio", "Mes"] = 6
df2['Año'] = df2['Año'].astype('float64')
df2['Mes'] = df2['Mes'].astype('float64')
df2.rename(columns = {'Año':'Year'}, inplace = True)

# Identificamos las comunidades autonomas para poder imprimirlas y revisar que el formato sea el mismo
ccaa2 = df2['CCAA'].drop_duplicates().tolist()
print(ccaa2)

# Cambiamos la variable CCAA para que los valores coincidan con el mismo formato
df['CCAA'] = df['CCAA'].replace({
     'Andalucía': 'Andalucia',
     'Aragón': 'Aragon',
     'Castilla y León': 'Castilla Leon',
     'Castilla-La Mancha': 'Castilla La Mancha',
     'Comunidad Foral de Navarra': 'Navarra',
     'Comunidad de Madrid': 'Madrid',
     'Comunitat Valenciana': 'Valencia',
     'Illes Balears': 'Baleares',
     'País Vasco': 'Pais Vasco',
     'Principado de Asturias': 'Asturias',
     'Región de Murcia': 'Murcia'
})

print(df2['CCAA'].nunique())
print(df['CCAA'].nunique())

print(df.dtypes)
print(df2.dtypes)

df.to_csv('dataframes_processed/covidCCAA_processed.csv', index=False)
df2.to_csv('dataframes_processed/consumoCCAA_processed.csv', index=False)

# Hacemos merge de los 2 dataframe mediante los 3 atributos que coincide y exportamos
result = pd.merge(df, df2, on=['Mes','Year','CCAA'])
result = result.loc[(result != 0).any(axis=1)]
result['TasaMortalidad'] = result['Fallecidos'] / result['CasosConfirmados']
result['TasaMortalidad'] = result['TasaMortalidad'].round(5)

# Eliminamos los valores de tasa de mortalidad que no esten dentro del rango establecido de 0 a 1
column = result['TasaMortalidad']
mask = (column >= 0) & (column <= 1)
result = result[mask]

# Eliminamos los ceros en todas las columnas cuantitativas
result = result[(result[['Volumen (miles de kg)','Penetración (%)', 'CasosConfirmados', 'Fallecidos']] != 0).all(axis=1)]

print(result.dtypes)
result.to_csv('dataframes_processed/marzo-junio-2020_CovidProductosCCAA.csv', index=False)

