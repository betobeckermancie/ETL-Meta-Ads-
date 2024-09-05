#Resultados del Analisis 
# Este boxplot muestra la distribución del número de personas alcanzadas por los anuncios en tu dataset.
# Aquí está el análisis del gráfico:

# 1. Mediana (línea central dentro de la caja):
#    - La mediana del número de personas alcanzadas es aproximadamente 10,000.
#    - Esto significa que el 50% de los anuncios alcanzaron menos de 10,000 personas, mientras que el otro 50% alcanzó más.

# 2. Caja (intercuartil, IQR):
#    - La caja representa el rango intercuartil (IQR), que abarca desde el primer cuartil (Q1) hasta el tercer cuartil (Q3).
#    - En este caso, el rango intercuartil se sitúa aproximadamente entre 7,500 y 15,000 personas alcanzadas.
#    - Este rango contiene el 50% central de los datos, lo que indica que la mayoría de los anuncios alcanzaron entre 7,500 y 15,000 personas.

# 3. Bigotes (whiskers):
#    - Los bigotes se extienden desde los límites de la caja (Q1 y Q3) hasta el valor máximo y mínimo dentro de 1.5 veces el IQR.
#    - En este gráfico, el bigote superior se extiende hasta aproximadamente 45,000 personas alcanzadas,
#      lo que sugiere que la mayoría de los datos no son considerados valores atípicos hasta este punto.

# 4. Valores atípicos (círculos rojos):
#    - Los puntos rojos representan los valores atípicos, que en este caso son los anuncios que alcanzaron más de 45,000 personas.
#    - Estos puntos son significativamente más altos que el resto de los datos y merecen un análisis adicional.
#    - Puede ser interesante investigar por qué estos anuncios tuvieron un alcance tan alto en comparación con los demás.

# Conclusión:
# - La mayoría de los anuncios en tu dataset alcanzaron entre 7,500 y 15,000 personas.
# - Hay unos pocos anuncios que lograron un alcance excepcionalmente alto, más de 45,000 personas, que son considerados valores atípicos.
# - Estos valores atípicos pueden ser el resultado de una estrategia publicitaria más efectiva o un mayor presupuesto destinado a esos anuncios específicos.
# - Vale la pena profundizar en las características de esos anuncios para entender mejor qué factores contribuyeron a su éxito.


#Boxplot para Columna personas_alcanzadas de anuncios
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
box=plt.boxplot(df['personas_alcanzadas'],patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

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
plt.title('Distribucion de personas alcanzadas por Anuncios', fontsize=16)
plt.ylabel('Numero de personas', fontsize=16)
plt.grid(True, linestyle='--', alpha=1)

#Ajustar el rango del eje 'Y' y los ticks
plt.ylim(0, df['personas_alcanzadas'].max()+500)#ajustar el limite superior del eje Y
plt.yticks(range(0, int(df['personas_alcanzadas'].max())+5000, 2500)) #configurar los ticks de 100 en 100

#Mostrar grafico
plt.show()

# Identificar límites del boxplot
q1 = df['personas_alcanzadas'].quantile(0.25)
q3 = df['personas_alcanzadas'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con personas alcanzadas por encima del límite superior
anuncios_outliers = df[df['personas_alcanzadas'] > upper_bound]

# Mostrar los nombres de los anuncios que son outliers
print("Anuncios con más personas alcanzadas (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'personas_alcanzadas']])