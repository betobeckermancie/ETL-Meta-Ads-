import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Asegurarse de que la columna date_start esté en formato de fecha
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])

# Seleccionar las columnas que especificar para sumar
columns_to_sum = ['clicks_en_anuncio', 'costo_por_click_anuncio', 'click_enlace_trafico', 'conversion_boton_msj']

# Agrupar por fecha y sumar las interacciones
df_grouped = df.groupby('fecha_inicio')[columns_to_sum].sum()

# Sumar las columnas seleccionadas para obtener el total de interacciones por fecha
df_grouped['total_interacciones'] = df_grouped.sum(axis=1)

# Crear el histograma para mostrar la distribución de interacciones a lo largo del tiempo (por fecha)
plt.figure(figsize=(10, 6))
plt.hist(df_grouped.index, weights=df_grouped['total_interacciones'], bins=30, color='skyblue')

# Formatear las fechas en el eje x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))

# Añadir etiquetas y título
plt.title('Histograma de Interacciones a lo largo del tiempo (por Fecha)')
plt.xlabel('Fecha')
plt.ylabel('Total de Interacciones')


# Mostrar el gráfico
plt.tight_layout()
plt.show()