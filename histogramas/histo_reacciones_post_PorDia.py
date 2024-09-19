import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Asegurarse de que la columna date_start esté en formato de fecha
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])

# Especificar el parámetro que deseas analizar
parametro_a_analizar = 'reacciones_post'  # Cambia este valor por la columna que deseas analizar

# Agrupar por fecha y sumar el parámetro seleccionado
df_grouped = df.groupby('fecha_inicio')[parametro_a_analizar].sum()

# Crear el histograma para mostrar la distribución del parámetro a lo largo del tiempo (por fecha)
plt.figure(figsize=(10, 6))
plt.hist(df_grouped.index, weights=df_grouped.values, bins=30, color='skyblue')

# Formatear las fechas en el eje x para que se muestren con el formato deseado
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Intervalo de 7 días

# Añadir etiquetas y título dinámico basado en el parámetro
plt.title(f'Histograma de {parametro_a_analizar} a lo largo del tiempo (por Fecha)')
plt.xlabel('Fecha')
plt.ylabel(f'Cantidad de {parametro_a_analizar}')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
