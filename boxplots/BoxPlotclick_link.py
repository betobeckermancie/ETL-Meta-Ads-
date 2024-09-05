# link_click
# - Número de clics en enlaces dentro del anuncio.
# - Indica cuántos usuarios interactuaron con los enlaces del anuncio, crucial para campañas orientadas a generar tráfico.

#Boxplot para Columna click_link de anuncios
# El análisis del boxplot es útil para identificar la dispersión de tus datos en otras palabras la distrucion de un conjunto de datos y resaltar los valores atipicos,
# entender la distribución central, y localizar posibles valores atípicos que
# podrían necesitar un análisis más detallado.

import matplotlib.pyplot as plt
import pandas as pd
#cargar el csv para analizar
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

#configurar las propiedades de los fliers(valores atipicos)
flierprops = dict(marker='o', markerfacecolor='red', markersize=5, linestyle='none')

#crear el grafico a detalle
plt.figure(figsize=(5,6))#Ajustar el tamano de grafico

#creando boxplot detallado
box=plt.boxplot(df['click_link'],patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

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
plt.title('Distribucion de click_link por Anuncios', fontsize=16)
plt.ylabel('click en el link', fontsize=16)
plt.grid(True, linestyle='--', alpha=1)

#Ajustar el rango del eje 'Y' y los ticks
#plt.ylim(0, df['click_link'].max()+500)#ajustar el limite superior del eje Y
plt.yticks(range(0, int(df['click_link'].max()), 100)) #configurar los ticks de 100 en 100

#Mostrar grafico
plt.show()

# Identificar límites del boxplot
q1 = df['click_link'].quantile(0.25)
q3 = df['click_link'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con mas click_link por encima del límite superior
anuncios_outliers = df[df['click_link'] > upper_bound]

# Mostrar los nombres de los anuncios que son outliers
print("Anuncios con más clicks en el link (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'click_link']])