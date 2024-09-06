#Descripción: Cantidad de interacciones con la publicación, como "Me gusta", comentarios y compartidos.
#Justificación: Esta métrica es importante para medir el interés y la interacción directa que generan tus anuncios, 
#lo cual es clave para campañas enfocadas en la construcción de marca y reconocimiento.

#Boxplot para Columna interaccion_post de anuncios

# El análisis del boxplot es útil para identificar la dispersión de tus datos en otras palabras la distrucion de un conjunto de datos y resaltar los valores atipicos,
# entender la distribución central, y localizar posibles valores atípicos que
# podrían necesitar un análisis más detallado.

import matplotlib.pyplot as plt
import pandas as pd
#cargar el csv para analizar
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

#configurar las propiedades de los fliers(valores atipicos)
flierprops = dict(marker='o', markerfacecolor='red', markersize=5, linestyle='none')

#crear el grafico a detalle
plt.figure(figsize=(5,6))#Ajustar el tamano de grafico

#creando boxplot detallado
box=plt.boxplot(df['interaccion_post'],patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

#Personalizar colores de la caja
for patch in box ['boxes']:
    patch.set_facecolor('lightblue')
#Personalizar colores de los bigotes y medianas
for whisker in box['whiskers']:
    whisker.set(color='black', linewidth=1.5)
#gorras
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
#mediana
for mean in box['means']:
    mean.set(marker='o',color='green', markersize=5)

#Etiquetas y titulo
plt.title('Distribucion de la interaccion con el Ad', fontsize=16)
plt.ylabel('Interaccion', fontsize=16)
plt.grid(True, linestyle='--', alpha=1)

#Ajustar el rango del eje 'Y' y los ticks
plt.ylim(0, df['interaccion_post'].max()+500)#ajustar el limite superior del eje Y
plt.yticks(range(0, int(df['interaccion_post'].max())+1000, 1000)) #configurar los ticks de 100 en 100

#Mostrar grafico
plt.show()

# Identificar límites del boxplot
q1 = df['interaccion_post'].quantile(0.25)
q3 = df['interaccion_post'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con mas interaccion_post por encima del límite superior
anuncios_outliers = df[df['interaccion_post'] > upper_bound]

# Mostrar los nombres de los anuncios que son outliers
print("Anuncios con más interaccion (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'interaccion_post']])