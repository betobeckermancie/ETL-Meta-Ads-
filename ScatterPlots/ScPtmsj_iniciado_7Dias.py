#comparamos la relacion que existe entre msj_iniciado_7Dias con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el msj_iniciado_7Dias
for column in numeric_columns:
    if column != 'msj_iniciado_7Dias':  # Saltar la columna 'msj_iniciado_7Dias' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="msj_iniciado_7Dias", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs msj_iniciado_7Dias')
        plt.xlabel(column)
        plt.ylabel('msj_iniciado_7Dias')
        
        # Mostrar el gráfico
        plt.show()
