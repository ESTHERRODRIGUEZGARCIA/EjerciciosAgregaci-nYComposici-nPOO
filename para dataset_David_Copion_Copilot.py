# importar librerias para dataset
import numpy as np
import pandas as pd

# importar librerias para modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# importar librerias para visualizar
import seaborn as sns
import matplotlib.pyplot as plt

# importar librerias para guardar
import pickle

# importar librerias para graficar
import  seaborn as sns

# leer dataset de ubicacion
dataset = pd.read_csv('dataset/dataset.csv')


# visualizar dataset
sns.pairplot(dataset)
plt.show()

#limpiar dataset
dataset.drop(['Unnamed: 0'], axis=1, inplace=True)

#deteccion de variables
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#deteccion de outliers
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#imprimir grafico de outliers
sns.pairplot(dataset)
plt.show()

#imprimir graficas de dataset
sns.pairplot(dataset)
plt.show()

#encontrar valores perdidos
dataset.isnull().sum()

#rellenar valores perdidos
dataset['Age'].fillna(dataset['Age'].mean(), inplace=True)


