import pandas as pd

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_renombrado.csv")

# Selecciona la columna que deseas analizar
column = 'spend'

# Calcular el IQR
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

# Definir los límites para identificar outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrar los outliers
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

print(outliers)
