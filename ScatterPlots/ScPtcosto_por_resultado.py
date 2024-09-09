#comparamos la relacion que existe entre costo_por_resultado con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el costo_por_resultado
for column in numeric_columns:
    if column != 'costo_por_resultado':  # Saltar la columna 'costo_por_resultado' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="costo_por_resultado", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs costo_por_resultado')
        plt.xlabel(column)
        plt.ylabel('costo_por_resultado')
        
        # Mostrar el gráfico
        plt.show()
