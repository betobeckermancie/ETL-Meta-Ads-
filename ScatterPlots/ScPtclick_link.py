#comparamos la relacion que existe entre conversion_boton_msj con todas las columnas 
#numericas existentes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear scatterplots comparándolas con el conversion_boton_msj
for column in numeric_columns:
    if column != 'conversion_boton_msj':  # Saltar la columna 'conversion_boton_msj' para no compararla consigo misma
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=column, y="conversion_boton_msj", data=df, color="blue")
        
        # Agregar etiquetas y títulos
        plt.title(f'Scatterplot de {column} vs conversion_boton_msj')
        plt.xlabel(column)
        plt.ylabel('conversion_boton_msj')
        
        # Mostrar el gráfico
        plt.show()