import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.txt', sep="|",decimal = "," )

X = df[['Penetración (%)', 'Precio medio kg', 'Consumo per capita']]
Y = df['Valor (miles de €)']

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
print(predictions)