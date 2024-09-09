#comparamos la relacion que existe entre click_enlace_trafico con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el click_enlace_trafico
for column in numeric_columns:
    if column != 'click_enlace_trafico':  # Saltar la columna 'click_enlace_trafico' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="click_enlace_trafico", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs click_enlace_trafico')
        plt.xlabel(column)
        plt.ylabel('click_enlace_trafico')
        
        # Mostrar el gráfico
        plt.show()