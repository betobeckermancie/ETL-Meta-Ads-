#Revisar si aplica boxplot para cada columna

#Distribución y Dispersión:
#Los histogramas te muestran cómo están distribuidos los datos en cada columna. Si #observas que la mayoría de los datos están concentrados en un rango específico pero #hay valores que parecen estar muy alejados (outliers), es una buena señal de que un #boxplot sería útil.
#Por ejemplo, en los histogramas donde ves una concentración de valores a la #izquierda (valores bajos) y una cola larga hacia la derecha, esto sugiere la #presencia de outliers, y un boxplot podría ayudar a visualizarlos mejor.

#Outliers Potenciales:
#Si en el histograma ves que hay algunos valores muy alejados de la masa principal de #datos, estos son candidatos a ser considerados outliers. El boxplot es ideal para #identificar visualmente estos outliers.

#Asimetria:
#Si el histograma muestra una distribución muy asimétrica, donde la mayoría de los #valores están en un lado y una cola larga en el otro, un boxplot puede ayudarte a #visualizar mejor la mediana, el rango intercuartil, y cómo los datos están #distribuidos en relación con la mediana.

import pandas as pd
import matplotlib.pyplot as plt

#cargar el csv para analizar 
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

#filtrar solo las columnas numericas
df_numeric = df.select_dtypes(include=['float64', 'int64'])

#crear historias para todas las columnas numericas
df_numeric.hist(figsize=(15,10), bins=30, edgecolor='black', linewidth=1.2)

#Ajustar el espacio entre los subplots
plt.tight_layout()

#Mostrar la grafica
plt.show()