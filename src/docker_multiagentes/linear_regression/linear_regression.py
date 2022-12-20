import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import psycopg2
from sqlalchemy import create_engine

engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

query = '''SELECT * FROM "data_iterativo.txt.processed"'''
df =pd.read_sql(query, engine)
print(df)
X = df[['Penetración (%)']]
y = df['Valor (miles de €)']

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
#df.insert(0,'prediction',predictions)
print(predictions)

#sns.scatterplot(x='Penetración (%)', y='Valor (miles de €)', data = df)

#sns.lineplot(x='Penetración (%)', y='prediction', data = df, color='red')
#plt.show()