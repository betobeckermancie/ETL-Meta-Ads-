# cpp
# - Costo por resultado (por ejemplo, compra, registro, etc.).
# - Evalúa la eficiencia del anuncio para obtener resultados específicos.

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
plt.figure(figsize=(5,10))#Ajustar el tamano de grafico

#creando boxplot detallado
box=plt.boxplot(df['costo_por_resultado'],patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

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
plt.title('Distribucion del costo por resultado de Anuncio', fontsize=16)
plt.ylabel('Costo($)', fontsize=14)
plt.grid(True, linestyle='--', alpha=1)

#Ajustar el rango del eje 'Y' y los ticks
plt.ylim(0, df['costo_por_resultado'].max()+1)  # Ajustar el límite superior del eje Y
plt.yticks(range(0, int(df['costo_por_resultado'].max())+2, 1))  # Configurar los ticks de 1 en 1


#Mostrar grafico
plt.show()

# Identificar límites del boxplot
q1 = df['costo_por_resultado'].quantile(0.25)
q3 = df['costo_por_resultado'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con mas costo_por_resultado por encima del límite superior
anuncios_outliers = df[df['costo_por_resultado'] > upper_bound]

#ordenar los outliners de mayor a menor por 'costo_por_resultado'
anuncios_outliers= anuncios_outliers.sort_values(by='costo_por_resultado', ascending=False)

# Mostrar los nombres de los anuncios que son outliers
print("Costo por resultado de anuncio (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'costo_por_resultado']])