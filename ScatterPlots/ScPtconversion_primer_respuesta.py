#comparamos la relacion que existe entre conversion_primer_respuesta con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el conversion_primer_respuesta
for column in numeric_columns:
    if column != 'conversion_primer_respuesta':  # Saltar la columna 'conversion_primer_respuesta' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="conversion_primer_respuesta", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs conversion_primer_respuesta')
        plt.xlabel(column)
        plt.ylabel('conversion_primer_respuesta')
        
        # Mostrar el gráfico
        plt.show()