import pandas as pd

# Cargar el DataFrame
df_ACC_TRA = pd.read_csv('/mnt/data/Data/Accidentes_de_transito_en_carreteras-2020-2021-Sutran.csv', encoding='utf8', delimiter=';')

# Configuración de pandas para mostrar todas las columnas y ajustar el ancho
pd.set_option('display.max_columns', 20)  # Mostrar un máximo de 20 columnas para una mejor visualización
pd.set_option('display.width', 1000)

# Definir las columnas a eliminar basándonos en los nombres exactos impresos
DROP_COLUMNS = ['FECHA_CORTE', 'FECHA', 'KILOMETRO', 'FALLECIDOS', 'HERIDOS']

# Eliminar las columnas especificadas
df_ACC_TRA.drop(columns=DROP_COLUMNS, inplace=True)

# Listado donde estan almacenados los campos relacionado al dataset de accidentes de transito
columnas_ACC_TRA = list(df_ACC_TRA.select_dtypes(include=['object']).columns)

def procesar_datos():
    global df_ACC_TRA

    # Eliminar registros que sean duplicados
    df_ACC_TRA = df_ACC_TRA.drop_duplicates() if df_ACC_TRA.duplicated().any() else df_ACC_TRA

    # Aplicar One-Hot Encoding a los campos 'MODALIDAD' y 'DEPARTAMENTO'
    df_ACC_TRA = pd.get_dummies(df_ACC_TRA, columns=['MODALIDAD', 'DEPARTAMENTO'])

    # Convertir solo las columnas de One-Hot Encoding a valores enteros (0 y 1)
    for column in df_ACC_TRA.columns:
        if 'MODALIDAD_' in column or 'DEPARTAMENTO_' in column:
            df_ACC_TRA[column] = df_ACC_TRA[column].astype(int)

procesar_datos()

# Mostrar las primeras 100 filas seleccionando solo algunas columnas para verificar el resultado
print("\nVista del DataFrame después de One-Hot Encoding:")
print(df_ACC_TRA.head(100)[['HORA', 'CODIGO_VIA'] + [col for col in df_ACC_TRA.columns if 'MODALIDAD_' in col or 'DEPARTAMENTO_' in col][:10]].to_string(index=False))

