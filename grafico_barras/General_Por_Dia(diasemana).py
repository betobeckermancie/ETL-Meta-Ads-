import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_general.csv")

# Asegurarse de que la columna 'date_start' está en formato de fecha
df['date_start'] = pd.to_datetime(df['date_start'])

# Crear una nueva columna con el día de la semana ('Monday', 'Tuesday', etc.)
df['dia_semana'] = df['date_start'].dt.day_name()

# Agrupar los datos por el día de la semana para calcular las interacciones
df_grouped = df.groupby('dia_semana').agg({
    'clicks_en_anuncio': 'sum',
    'veces_mostrado': 'sum',
    'click_enlace_trafico': 'sum',  # Añade otras métricas relevantes que desees
    'interaccion_post': 'sum',
    'conversion_boton_msj': 'sum',
    'contenido_guardado':'sum'
}).reset_index()

# Crear una columna que sume todas las interacciones
df_grouped['total_interacciones'] = (
    df_grouped['clicks_en_anuncio'] + 
    df_grouped['veces_mostrado'] + 
    df_grouped['click_enlace_trafico'] + 
    df_grouped['interaccion_post']+
    df_grouped['conversion_boton_msj']+
    df_grouped['contenido_guardado']
)

# Ordenar los días de la semana en el orden correcto
dias_orden = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
df_grouped['dia_semana'] = pd.Categorical(df_grouped['dia_semana'], categories=dias_orden, ordered=True)
df_grouped = df_grouped.sort_values('dia_semana')

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_grouped['dia_semana'], df_grouped['total_interacciones'], color='blue')

# Etiquetas y título
plt.title('Total de Interacciones por Día de la Semana', fontsize=16)
plt.xlabel('Día de la Semana', fontsize=14)
plt.ylabel('Total de Interacciones', fontsize=14)

# Mostrar gráfico
plt.tight_layout()
plt.show()
