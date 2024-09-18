import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Asegurarse de que la columna date_start esté en formato de fecha
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])

# Extraer el día de la semana (Monday=0, Sunday=6)
df['day_of_week'] = df['fecha_inicio'].dt.dayofweek

# Mapear los valores numéricos a los nombres de los días
dias_semana = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
df['day_of_week'] = df['day_of_week'].map(dias_semana)

#selecionamos las columnas especificar a sumar
columns_to_sum =['clicks_en_anuncio','costo_por_click_anuncio','click_enlace_trafico','conversion_boton_msj']

# Agrupar por el día de la semana y sumar las interacciones
df_grouped = df.groupby('day_of_week')[columns_to_sum].sum()

#sumar las columnas seleccionadas para obtener el total de interacciones por dia
df_grouped['total_interacciones']=df_grouped.sum(axis=1)

# Ordenar los días de la semana correctamente
df_grouped = df_grouped.reindex(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])

# Crear el gráfico de barras usando solo la columna 'total_interacciones'
plt.figure(figsize=(10, 6))
df_grouped['total_interacciones'].plot(kind='bar', color='skyblue')

# Añadir etiquetas y título
plt.title('Total de Interacciones por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Cantidad')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
