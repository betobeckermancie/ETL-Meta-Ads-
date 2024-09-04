import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV en un DataFrame
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

# Asegurarse de que las columnas de fecha están en el formato de fecha adecuado
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])
df['fecha_finalizacion'] = pd.to_datetime(df['fecha_finalizacion'])

# Calcular la diferencia de días entre la fecha de inicio y la fecha de finalización
df['dias_duracion'] = (df['fecha_finalizacion'] - df['fecha_inicio']).dt.days

# Calcular el promedio de clicks en el link al dia (evitando la división por 0)
df['clicks_por_dia'] = df['click_link'] / df['dias_duracion'].replace(0, 1)

# Agrupar por nombre de anuncio y calcular el promedio de clciks en el link al dia
promedio_clicks_por_dia = df.groupby('nombre_anuncio')['clicks_por_dia'].mean().sort_values(ascending=False)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
ax = promedio_clicks_por_dia.plot(kind='bar', color='skyblue')
plt.title('Promedio de click en el link por Dia', fontsize=16)
plt.xlabel('Nombre del Anuncio', fontsize=14)
plt.ylabel('Promedio', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Rotar las etiquetas del eje X para mejorar la legibilidad
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')

# Ajustar el diseño para que se vea bien
plt.tight_layout()

# Mostrar el gráfico
plt.show()