import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Asegurarse de que las columnas de fecha estén en formato datetime
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
df['fecha_finalizacion'] = pd.to_datetime(df['fecha_finalizacion'])

# Filtrar solo las columnas numéricas
numeric_columns = df.select_dtypes(include='number').columns

# Iterar sobre todas las columnas numéricas y crear gráficos de líneas comparándolas con la fecha de inicio
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    
    # Crear un gráfico de líneas con la fecha en el eje x y el valor numérico en el eje y
    plt.plot(df['fecha_inicio'], df[column], marker='o')
    
    # Agregar etiquetas y títulos
    plt.title(f'Gráfico de Líneas de {column} vs Fecha de Inicio', fontsize=16)
    plt.xlabel('Fecha de Inicio', fontsize=14)
    plt.ylabel(column, fontsize=14)
    
    # Rotar las etiquetas de fecha en el eje x para mayor legibilidad
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()  # Asegurarse de que los elementos no se superpongan
    plt.grid(True)
    plt.show()
