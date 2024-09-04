import pandas as pd
import matplotlib.pyplot as plt

#cargar el csv en un dataframe
df= pd.read_csv ("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

#asegurar que las columnas fecha este en el formato correcto
df['fecha_inicio']= pd.to_datetime(df['fecha_inicio'])
df['fecha_finalizacion'] = pd.to_datetime(df['fecha_finalizacion'])

#calcular la diferencia entre fecha de inicio y finalizacion
df['dias_duracion']= (df['fecha_finalizacion']-df['fecha_inicio']).dt.days 

#Calcular el promedio por de clicks por dia(evitando dividir entre 0)
df['clicks_por_dia']= df['click_enlace_trafico']/df['dias_duracion'].replace(0,1)

#Agrupar por nombre de anuncio y calcular el promedio de clicks por dia
promedio_clicks_por_dia=df.groupby('nombre_anuncio')['clicks_por_dia'].mean().sort_values(ascending=False)

#crea grafico de barras
plt.figure(figsize=(10,6))
ax=promedio_clicks_por_dia.plot(kind='bar', color='red')
plt.title('Promedio de clicks en link por dia en anuncio', fontsize=16)
plt.xlabel('Nombre del anuncio', fontsize=14)
plt.ylabel('Promedio', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

#rotar las etiquetas para mejorar la visualizacion
ax.set_xticklabels(ax.get_xticklabels(), rotation =90,ha='right')

#ajustar el diseño para que se vea mejor
plt.tight_layout()

#mostrar
plt.show()