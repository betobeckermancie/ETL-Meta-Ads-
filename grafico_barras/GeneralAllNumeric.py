import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear gráficos de barras
for column in numeric_columns:
    # Agrupar por 'nombre_anuncio' y sumar los valores
    grouped_df = df.groupby('nombre_anuncio')[column].sum().sort_values(ascending=False)
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    ax = grouped_df.plot(kind='bar')
    plt.title(f'Gráfico de Barras de {column}', fontsize=16)
    plt.xlabel('Nombre del Anuncio', fontsize=14)
    plt.ylabel(column, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Mostrar el gráfico
    plt.tight_layout()  # Asegurar que todo se vea bien
    plt.show()