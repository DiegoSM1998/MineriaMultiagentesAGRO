#!/usr/bin/python3
# -- coding: utf-8 --
'''Preprocesamiento datos raw'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DIR = "Dataset1.- DatosConsumoAlimentarioMAPAporCCAA.txt"
raw = pd.read_csv(DIR, sep="|", decimal=",")

raw.drop(raw.columns[[ -1,-2,-3,-4]], axis=1, inplace = True)
#Elimino las columnas que no usare o tienen fallos

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

procesed['Penetración (%)'] = procesed['Penetración (%)'].fillna(raw['Penetración (%)'].mean())
null_values = procesed.isnull().sum()
print(f"Num de variables nulas por columna:\n {null_values}")
#En este caso vemos que hay valores NaN,
#la forma de tratarlos sera sustituirlos por la media ya que 
#corresponden con los datos de los utlimos meses que seran los
#se sometan a prueba y no los de entremaniento

procesed= pd.get_dummies(procesed, columns=["Mes","Producto"])
#Aplico la codificación de one-hot para las variables categoricas

processedTNacional=procesed[procesed['CCAA'] == "Total Nacional"]
#Separo el total nacional 

processedTNacional=processedTNacional.drop('CCAA',axis=1)
#Elimino la columna CCAA al ser todas la misma

print(processedTNacional.dtypes)

mask = ((processedTNacional['Año']==2020) & (
    (processedTNacional['Mes_Enero']!= 1) | (processedTNacional['Mes_Febrero'] != 1)))

# Seleccionar las variables que queremos usar como variables independientes
# y la variable dependiente
x_train = processedTNacional[~mask][['Año', 'Mes_Abril', 'Mes_Agosto','Mes_Diciembre',
       'Mes_Enero', 'Mes_Febrero', 'Mes_Julio', 'Mes_Junio', 'Mes_Marzo',
       'Mes_Mayo', 'Mes_Noviembre', 'Mes_Octubre', 'Mes_Septiembre',
       'Producto_AGUACATE', 'Producto_AJOS', 'Producto_ALBARICOQUES',
       'Producto_ALCACHOFAS', 'Producto_APIO', 'Producto_BERENJENAS',
       'Producto_BROCOLI', 'Producto_CALABACINES', 'Producto_CEBOLLAS',
       'Producto_CEREZAS', 'Producto_CHAMPIÑONES+O.SETAS',
       'Producto_CHIRIMOYA', 'Producto_CIRUELAS', 'Producto_COLES',
       'Producto_COLIFLOR', 'Producto_ESPARRAGOS', 'Producto_FRESAS/FRESON',
       'Producto_FRUTAS IV GAMA', 'Producto_JUDIAS VERDES', 'Producto_KIWI',
       'Producto_LECHUGA/ESC./ENDIVIA', 'Producto_LIMONES',
       'Producto_MANDARINAS', 'Producto_MANGO', 'Producto_MANZANAS',
       'Producto_MELOCOTONES', 'Producto_MELON', 'Producto_NARANJAS',
       'Producto_NECTARINAS', 'Producto_OTR.HORTALIZAS/VERD.',
       'Producto_OTRAS FRUTAS FRESCAS', 'Producto_PATATAS CONGELADAS',
       'Producto_PATATAS FRESCAS', 'Producto_PATATAS FRITAS',
       'Producto_PATATAS PROCESADAS', 'Producto_PEPINOS', 'Producto_PERAS',
       'Producto_PIMIENTOS', 'Producto_PIÑA', 'Producto_PLATANOS',
       'Producto_POMELO', 'Producto_PUERRO', 'Producto_SANDIA',
       'Producto_T.FRUTAS FRESCAS', 'Producto_T.HORTALIZAS FRESCAS',
       'Producto_TOMATES', 'Producto_TOTAL PATATAS', 'Producto_UVAS',
       'Producto_VERD./HORT. IV GAMA', 'Producto_VERDURAS DE HOJA',
       'Producto_ZANAHORIAS']]

y_train = processedTNacional[~mask][['Volumen (miles de kg)',
        'Valor (miles de €)','Precio medio kg', 'Penetración (%)']]

x_test = processedTNacional[mask][['Año', 'Mes_Abril', 'Mes_Agosto','Mes_Diciembre',
       'Mes_Enero', 'Mes_Febrero', 'Mes_Julio', 'Mes_Junio', 'Mes_Marzo',
       'Mes_Mayo', 'Mes_Noviembre', 'Mes_Octubre', 'Mes_Septiembre',
       'Producto_AGUACATE', 'Producto_AJOS', 'Producto_ALBARICOQUES',
       'Producto_ALCACHOFAS', 'Producto_APIO', 'Producto_BERENJENAS',
       'Producto_BROCOLI', 'Producto_CALABACINES', 'Producto_CEBOLLAS',
       'Producto_CEREZAS', 'Producto_CHAMPIÑONES+O.SETAS',
       'Producto_CHIRIMOYA', 'Producto_CIRUELAS', 'Producto_COLES',
       'Producto_COLIFLOR', 'Producto_ESPARRAGOS', 'Producto_FRESAS/FRESON',
       'Producto_FRUTAS IV GAMA', 'Producto_JUDIAS VERDES', 'Producto_KIWI',
       'Producto_LECHUGA/ESC./ENDIVIA', 'Producto_LIMONES',
       'Producto_MANDARINAS', 'Producto_MANGO', 'Producto_MANZANAS',
       'Producto_MELOCOTONES', 'Producto_MELON', 'Producto_NARANJAS',
       'Producto_NECTARINAS', 'Producto_OTR.HORTALIZAS/VERD.',
       'Producto_OTRAS FRUTAS FRESCAS', 'Producto_PATATAS CONGELADAS',
       'Producto_PATATAS FRESCAS', 'Producto_PATATAS FRITAS',
       'Producto_PATATAS PROCESADAS', 'Producto_PEPINOS', 'Producto_PERAS',
       'Producto_PIMIENTOS', 'Producto_PIÑA', 'Producto_PLATANOS',
       'Producto_POMELO', 'Producto_PUERRO', 'Producto_SANDIA',
       'Producto_T.FRUTAS FRESCAS', 'Producto_T.HORTALIZAS FRESCAS',
       'Producto_TOMATES', 'Producto_TOTAL PATATAS', 'Producto_UVAS',
       'Producto_VERD./HORT. IV GAMA', 'Producto_VERDURAS DE HOJA',
       'Producto_ZANAHORIAS']]

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
plt.savefig('regression_model.png')
plt.show()