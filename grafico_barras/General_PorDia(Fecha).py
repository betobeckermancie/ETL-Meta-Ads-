#importamos las libreserias que se necesitan
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Agrupar los datos por 'fecha_inicio' para calcular las interacciones por día  agregando todas las metricas para que sean sumadas  en un grupo
df_grouped = df.groupby('fecha_inicio').agg({
    'clicks_en_anuncio': 'sum',
    'veces_mostrado': 'sum',
    'click_enlace_trafico': 'sum',  # Añade otras métricas relevantes que desees
    'interaccion_post': 'sum',
    'conversion_boton_msj': 'sum',
    'contenido_guardado':'sum'
}).reset_index()

# Crear una columna que sume todas las interacciones para cada día
df_grouped['total_interacciones'] = (
    df_grouped['clicks_en_anuncio'] + 
    df_grouped['veces_mostrado'] + 
    df_grouped['click_enlace_trafico'] + 
    df_grouped['interaccion_post']+
    df_grouped['conversion_boton_msj']+
    df_grouped['contenido_guardado']
)

# Ordenar el dataframe por 'total_interacciones' de mayor a menor
df_grouped = df_grouped.sort_values(by='total_interacciones', ascending=False)

# Crear gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(df_grouped['fecha_inicio'], df_grouped['total_interacciones'], color='blue')

# Etiquetas y título
plt.title('Total de Interacciones por Día', fontsize=16)
plt.xlabel('Fecha', fontsize=14)
plt.ylabel('Total de Interacciones', fontsize=14)
plt.xticks(rotation=90)  # Rotar las etiquetas de los días para mejor legibilidad

# Mostrar gráfico
plt.tight_layout()  # Para ajustar los elementos y que se vean correctamente
plt.show()
