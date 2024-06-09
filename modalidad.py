import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.base import TransformerMixin
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Cargar el archivo CSV desde la carpeta data
df = pd.read_csv('data/Accidentes de tránsito en carreteras-2020-2021-Sutran.csv', encoding='utf-8-sig', delimiter=';')

# Mostrar las primeras filas del DataFrame
print(df.head(50))

# Definir las columnas a eliminar basándonos en los nombres exactos impresos
DROP_COLUMNS = ['FECHA_CORTE', 'FECHA', 'KILOMETRO', 'FALLECIDOS', 'HERIDOS']

# Eliminar las columnas especificadas
df.drop(columns=DROP_COLUMNS, inplace=True)

# Mostrar las primeras filas del DataFrame después de eliminar las columnas
print(df.head(50))

# Aplicar One-Hot Encoding al campo 'MODALIDAD'
df_one_hot_modalidad = pd.get_dummies(df, columns=['MODALIDAD'])

# Convertir solo las columnas de One-Hot Encoding a valores enteros (0 y 1)
for column in df_one_hot_modalidad.columns:
    if 'MODALIDAD_' in column:
        df_one_hot_modalidad[column] = df_one_hot_modalidad[column].astype(int)

# Mostrar las primeras filas para verificar el resultado
print(df_one_hot_modalidad.head(50))
