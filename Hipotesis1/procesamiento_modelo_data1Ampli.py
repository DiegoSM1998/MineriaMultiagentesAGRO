#!/usr/bin/python3
# -- coding: utf-8 --
'''Preprocesamiento datos raw'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DIR = "Dataset1.1.-DatosConsumoAlimentario_2013-2020.txt"
raw = pd.read_csv(DIR, sep="|", decimal=",")
print(raw)
raw.drop(raw.columns[[ -1,-2,-3,-4]], axis=1, inplace = True)
#Elimino las columnas que no usare o tienen fallos

#print(raw.describe())
#Muestra las estadísticas de los datos
 
#Muestra los tipos de las columnasç
raw['Volumen (miles de kg)'] = raw['Volumen (miles de kg)'].str.replace('.', '').str.replace(',', '.')
raw['Volumen (miles de kg)'] = pd.to_numeric(raw['Volumen (miles de kg)'])

raw['Valor (miles de €)'] = raw['Valor (miles de €)'].str.replace('.', '').str.replace(',', '.')
raw['Valor (miles de €)'] = pd.to_numeric(raw['Valor (miles de €)'])

print(raw.dtypes)

zero_values = raw.eq(0).sum()
print(f"Num de variables nulas por columna:\n {zero_values}")
#muestra el número de valores igual a 0 por columna

procesed = raw[raw['Volumen (miles de kg)'] != 0]
#elimina las filas donde el volumen es igual a 0

null_values = procesed.isnull().sum()
print(f"Num de variables nulas por columna:\n {null_values}")
#En este caso vemos que no hay valores NaN

procesed= pd.get_dummies(procesed, columns=["Mes","Producto"])
#Aplico la codificación de one-hot para las variables categoricas

processedTNacional=procesed.drop('CCAA',axis=1)
#Elimino la columna CCAA al ser todas la misma

mask = ((processedTNacional['Año']==2020) & (
    (processedTNacional['Mes_ Enero']!= 1) | (processedTNacional['Mes_ Febrero'] != 1)))

# Seleccionar las variables que queremos usar como variables independientes
# y la variable dependiente
x_train = processedTNacional[~mask][['Año','Mes_ Abril', 'Mes_ Agosto', 'Mes_ Diciembre',
       'Mes_ Enero', 'Mes_ Febrero', 'Mes_ Julio', 'Mes_ Junio', 'Mes_ Marzo',
       'Mes_ Mayo', 'Mes_ Noviembre', 'Mes_ Octubre', 'Mes_ Septiembre',
       'Producto_ALCACHOFAS', 'Producto_BROCOLI',
       'Producto_CHAMPIÑOSNES+SETAS', 'Producto_COLIFLOR',
       'Producto_ESPARRAGOS', 'Producto_ESPINACAS',
       'Producto_FRUTA CONS/ALMIBAR', 'Producto_FRUTA EN CONSERVA',
       'Producto_FRUTA ESCARCHADA', 'Producto_FRUTAS CONGELADAS',
       'Producto_GUISANTES', 'Producto_JUDIA VERDE', 'Producto_JUDIAS VERDES',
       'Producto_MAIZ DULCE', 'Producto_MENESTRA',
       'Producto_MERMELADAS,CONFIT.', 'Producto_OTR.VERD/HOR.CONG.',
       'Producto_OTRA VERD/HORT.CON', 'Producto_PIMIENTOS',
       'Producto_RESTO FRUTA CONSER', 'Producto_TOMATE FRITO',
       'Producto_TOMATE N.ENTERO', 'Producto_TOMATE N.TRITUR.',
       'Producto_TOMATE NATURAL', 'Producto_TOMATES',
       'Producto_VERD./HORT.CONGELAD']]

y_train = processedTNacional[~mask][['Volumen (miles de kg)',
        'Valor (miles de €)','Precio medio kg', 'Penetración (%)']]

x_test = processedTNacional[mask][['Año','Mes_ Abril', 'Mes_ Agosto', 'Mes_ Diciembre',
       'Mes_ Enero', 'Mes_ Febrero', 'Mes_ Julio', 'Mes_ Junio', 'Mes_ Marzo',
       'Mes_ Mayo', 'Mes_ Noviembre', 'Mes_ Octubre', 'Mes_ Septiembre',
       'Producto_ALCACHOFAS', 'Producto_BROCOLI',
       'Producto_CHAMPIÑOSNES+SETAS', 'Producto_COLIFLOR',
       'Producto_ESPARRAGOS', 'Producto_ESPINACAS',
       'Producto_FRUTA CONS/ALMIBAR', 'Producto_FRUTA EN CONSERVA',
       'Producto_FRUTA ESCARCHADA', 'Producto_FRUTAS CONGELADAS',
       'Producto_GUISANTES', 'Producto_JUDIA VERDE', 'Producto_JUDIAS VERDES',
       'Producto_MAIZ DULCE', 'Producto_MENESTRA',
       'Producto_MERMELADAS,CONFIT.', 'Producto_OTR.VERD/HOR.CONG.',
       'Producto_OTRA VERD/HORT.CON', 'Producto_PIMIENTOS',
       'Producto_RESTO FRUTA CONSER', 'Producto_TOMATE FRITO',
       'Producto_TOMATE N.ENTERO', 'Producto_TOMATE N.TRITUR.',
       'Producto_TOMATE NATURAL', 'Producto_TOMATES',
       'Producto_VERD./HORT.CONGELAD']]

y_test = processedTNacional[mask][['Volumen (miles de kg)',
        'Valor (miles de €)','Precio medio kg', 'Penetración (%)']]

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con el conjunto de entrenamiento
model.fit(x_train, y_train)

# Evaluar el modelo con el conjunto de prueba
score = model.score(x_test, y_test)

print(f"El modelo tiene una precisión del {score*100:.2f}%")

import matplotlib.pyplot as plt

y_pred = model.predict(x_test)

y_test = y_test.assign(Prediccion_Volumen=y_pred[:,0])
y_test = y_test.assign(P_valor=y_pred[:,1])
y_test = y_test.assign(P_precio=y_pred[:,2])
y_test = y_test.assign(P_penetración=y_pred[:,3])

print(y_test)
y_test.plot(y=["Volumen (miles de kg)","Prediccion_Volumen"], kind='line')
plt.savefig('regression_AMPLImodel.png')
plt.show()