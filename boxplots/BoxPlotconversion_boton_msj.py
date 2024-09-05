# conversion_boton_msj
# es útil para evaluar la efectividad de las campañas que incluyen un componente 
# de mensajería como parte de su objetivo. Por ejemplo, si estás utilizando anuncios para fomentar consultas de productos o servicio al cliente a través de Messenger, esta métrica te indicará cuántas de esas conversiones han resultado en interacciones de mensajería.
# Puedes utilizar esta información para ajustar y optimizar tus campañas, 
# especialmente en términos de llamadas a la acción y mensajes dentro de los anuncios.

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
box=plt.boxplot(df['conversion_boton_msj'],patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

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
plt.title('Distribucion de conversion por msj', fontsize=16)
plt.ylabel('Efectividad', fontsize=14)
plt.grid(True, linestyle='--', alpha=1)

#Ajustar el rango del eje 'Y' y los ticks
plt.ylim(0, df['conversion_boton_msj'].max()+1)  # Ajustar el límite superior del eje Y
plt.yticks(range(0, int(df['conversion_boton_msj'].max())+2, 1))  # Configurar los ticks de 1 en 1


#Mostrar grafico
plt.show()

# Identificar límites del boxplot
q1 = df['conversion_boton_msj'].quantile(0.25)
q3 = df['conversion_boton_msj'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con mas conversion_boton_msj por encima del límite superior
anuncios_outliers = df[df['conversion_boton_msj'] > upper_bound]

#ordenar los outliners de mayor a menor por 'conversion_boton_msj'
anuncios_outliers= anuncios_outliers.sort_values(by='conversion_boton_msj', ascending=False)

# Mostrar los nombres de los anuncios que son outliers
print("Conversion por boton en mensaje (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'conversion_boton_msj']])