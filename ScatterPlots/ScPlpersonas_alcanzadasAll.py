#comparamos la relacion que existe entre personas_alcanzadas con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el personas_alcanzadas
for column in numeric_columns:
    if column != 'personas_alcanzadas':  # Saltar la columna 'personas_alcanzadas' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="personas_alcanzadas", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs personas_alcanzadas')
        plt.xlabel(column)
        plt.ylabel('personas_alcanzadas')
        
        # Mostrar el gráfico
        plt.show()
