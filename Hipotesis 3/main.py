#!/usr/bin/python3
# -- coding: utf-8 --
'''Hipótesis 3'''

import pandas as pd
import matplotlib.pyplot as plt
import io
import unidecode
import seaborn as sns
from sklearn.model_selection import train_test_split
DIR = "Dataset1.- DatosConsumoAlimentarioMAPAporCCAA.txt"
df = pd.read_csv(DIR, sep="|", decimal=",")


dfCov = pd.read_csv('Dataset5_Coronavirus_cases.txt', sep="|", decimal=",")
dfCov2 = dfCov[dfCov['countriesAndTerritories'].isin(['Spain'])]

#print(dfCov2)

superalimentos = []
with open("superalimentos.txt", 'r', encoding='utf8') as archivo:
	lineas = archivo.readlines()
	for linea in lineas:
		superalimentos.append(unidecode.unidecode(linea.strip('\n')).upper())
#print (superalimentos)

df2 = df[df['Producto'].isin(superalimentos)]
df3 = df2[df2['CCAA'].isin(['Total Nacional'])]
df3.drop(df.columns[[ 4, 5, 6, 9, -1,-2]], axis=1, inplace = True)
df4 = df3[df3['Producto'].isin(['UVAS'])]
df3['Penetración (%)'] = df3['Penetración (%)'].fillna(df4['Penetración (%)'].mean())
#Completo los valores NAN de las uvas con la penetración media de las mismas
df3 = df3.drop('CCAA',axis=1)

dfCov2.rename(columns={'year':'Año', 'month':'Mes'}, inplace=True)
dfCov2['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'] = dfCov2['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'].fillna(0)
meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
         7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

# Aplicamos el diccionario a la columna "Mes" usando el método map
dfCov2['Mes'] = dfCov2['Mes'].map(meses)
#df3.to_csv('DatosConsumoSuperalimentos.csv', index=False)
# print(df3)
result = pd.merge(dfCov2, df3, on=['Mes','Año'])
result.drop(result.columns[[ 0, 6, 7, 8, 9, 10]], axis=1, inplace = True)
#Elimino las columnas inncesarias
print(result)
result.to_csv('PenetracionSuperalimentosCasosCovid.csv', index=False)

mask = ((result['Año']==2020) & ((result['Mes']!= 'Enero')))
result2 = result[mask]
#Selección de datos deseados a través de una máscara
result2 = result2[['Mes','Producto','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]

maskAjos = ((result['Producto']=='AJOS'))
maskAguacate = ((result['Producto']=='AGUACATE'))
maskBrocoli = ((result['Producto']=='BROCOLI'))
maskColiflor = ((result['Producto']=='COLIFLOR'))
maskUvas = ((result['Producto']=='UVAS'))
r2AJOS = result2[maskAjos]
r2AGUACATE = result2[maskAguacate]
r2BROCOLI = result2[maskBrocoli]
r2COLIFLOR = result2[maskColiflor]
r2UVAS = result2[maskUvas]
r2AJOS = r2AJOS[['Mes','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]
r2AGUACATE = r2AGUACATE[['Mes','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]
r2BROCOLI = r2BROCOLI[['Mes','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]
r2COLIFLOR = r2COLIFLOR[['Mes','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]
r2UVAS = r2UVAS[['Mes','cases','deaths', 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', 'Penetración (%)','Consumo per capita']]
# matriz = result.corr()
# print(matriz)

sns.pairplot(r2AJOS, kind = 'reg')
plt.savefig('CovidAjosPenetracion.png')
plt.show()
plt.clf()

sns.pairplot(r2AGUACATE, kind = 'reg')
plt.savefig('CovidAguacatePenetracion.png')
plt.show()
plt.clf()

sns.pairplot(r2BROCOLI, kind = 'reg')
plt.savefig('CovidBrocoliPenetracion.png')
plt.show()
plt.clf()

sns.pairplot(r2COLIFLOR, kind = 'reg')
plt.savefig('CovidColiflorPenetracion.png')
plt.show()
plt.clf()

sns.pairplot(r2UVAS, kind = 'reg')
plt.savefig('CovidUvasPenetracion.png')
plt.show()
plt.clf()