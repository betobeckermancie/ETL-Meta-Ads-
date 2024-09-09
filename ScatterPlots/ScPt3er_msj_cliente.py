#comparamos la relacion que existe entre 3er_msj_cliente con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el 3er_msj_cliente
for column in numeric_columns:
    if column != '3er_msj_cliente':  # Saltar la columna '3er_msj_cliente' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="3er_msj_cliente", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs 3er_msj_cliente')
        plt.xlabel(column)
        plt.ylabel('3er_msj_cliente')
        
        # Mostrar el gráfico
        plt.show()
