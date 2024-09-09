#comparamos la relacion que existe entre interaccion_page con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el interaccion_page
for column in numeric_columns:
    if column != 'interaccion_page':  # Saltar la columna 'interaccion_page' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="interaccion_page", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs interaccion_page')
        plt.xlabel(column)
        plt.ylabel('interaccion_page')
        
        # Mostrar el gráfico
        plt.show()