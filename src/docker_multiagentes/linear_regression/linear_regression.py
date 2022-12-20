import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

engine = create_engine("postgresql://docker:docker@host.docker.internal/AGROdb")

query = '''SELECT * FROM "data_iterativo.txt.processed"'''
df =pd.read_sql(query, engine)

print(df)
explicativas = df[['Consumo per capita']]
objetivo = df['Gasto per capita']

model = LinearRegression()
model.fit(X = explicativas, y = objetivo)

predictions = model.predict(df[['Consumo per capita']])
df.insert(0,'prediction',predictions)
print(predictions)
print(df)
sns.scatterplot(x='Consumo per capita', y='Gasto per capita', data = df)
sns.scatterplot(x='Consumo per capita', y='prediction', data = df)
plt.savefig('data/regression_model.png')
plt.show()