# -*- coding: utf-8 -*-
#!/usr/bin/python3
# -- coding: utf-8 --
'''Preprocesamiento datos raw'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DIR = "Dataset1.1.-DatosConsumoAlimentario_2013-2020.txt"
raw = pd.read_csv(DIR, sep="|", decimal=",")

raw.drop(raw.columns[[ -1,-2,-5,-6,-7]], axis=1, inplace = True)
#Elimino las columnas que no usare o tienen fallos
raw['Volumen (miles de kg)'] = raw['Volumen (miles de kg)'].str.replace('.', '').str.replace(',', '.')
raw['Volumen (miles de kg)'] = pd.to_numeric(raw['Volumen (miles de kg)'])
#print(raw.describe())
#Muestra las estadísticas de los datos

print(raw.dtypes) 
#Muestra los tipos de las columnas

zero_values = raw.eq(0).sum()
#print(f"Num de variables nulas por columna:\n {zero_values}")
#muestra el número de valores igual a 0 por columna

procesed = raw[raw['Volumen (miles de kg)'] != 0]
#elimina las filas donde el volumen es igual a 0

zero_values = procesed.eq(0).sum()
#print(f"Num de variables nulas por columna:\n {zero_values}")
#muestra el número de valores igual a 0 por columna


#En este caso vemos que hay valores NaN,
#la forma de tratarlos sera sustituirlos por la media ya que 
#corresponden con los datos de los utlimos meses que seran los
#se sometan a prueba y no los de entremaniento

procesed= pd.get_dummies(procesed, columns=["Mes","Producto"])
#Aplico la codificación de one-hot para las variables categoricas
print(procesed.dtypes)
processedTNacional=procesed[procesed['CCAA'] == "Total nacional"]
#Separo el total nacional 

processedTNacional=processedTNacional.drop('CCAA',axis=1)
#Elimino la columna CCAA al ser todas la misma

print(processedTNacional.dtypes)

maskBefore2018 = (processedTNacional['Año']<=2017) 
mask2018 = (processedTNacional['Año']==2018)
mask2019 = (processedTNacional['Año']==2019)
mask2020 = (processedTNacional['Año']==2020)

raw

procesed

def modelo(maskTrain,maskTest):
  # Seleccionar las variables que queremos usar como variables independientes
  # y la variable dependiente
  x_train = processedTNacional[maskTrain][['Año','Mes_ Abril', 'Mes_ Agosto', 'Mes_ Diciembre',
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

  y_train = processedTNacional[maskTrain][['Consumo per capita',
          'Gasto per capita']]

  x_test = processedTNacional[maskTest][['Año','Mes_ Abril', 'Mes_ Agosto', 'Mes_ Diciembre',
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

  y_test = processedTNacional[maskTest][['Consumo per capita',
          'Gasto per capita']]

  # Crear el modelo de regresión lineal
  model = LinearRegression()

  # Entrenar el modelo con el conjunto de entrenamiento
  model.fit(x_train, y_train)

  # Evaluar el modelo con el conjunto de prueba
  score = model.score(x_test, y_test)

  print(f"El modelo tiene una precisión del {score*100:.2f}%")

  import matplotlib.pyplot as plt

  y_pred = model.predict(x_test)
  

  y_test = y_test.assign(Prediccion_Consumo=y_pred[:,0])
  y_test = y_test.assign(Prediccion_Gasto=y_pred[:,1])
  

 
  y_test.plot(y=["Consumo per capita","Prediccion_Consumo"], kind='line')
  y_test.plot(y=["Gasto per capita","Prediccion_Gasto"], kind='line')
  
  
  plt.savefig('regression_model_consumo.png')
  plt.show()

modelo(maskBefore2018, mask2018)

modelo(maskBefore2018, mask2019)

modelo(maskBefore2018, mask2020)