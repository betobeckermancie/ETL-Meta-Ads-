import matplotlib.pyplot as plt
import pandas as pd

#cargar el csv para analizar
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Total/anuncios_insights_general_total_limpiado.csv")

#ordenar los anuncios de mayor a menos por la columna 'personas_alcanzadas'
df_sorted= df.sort_values(by='personas_alcanzadas', ascending=False)

#configurar propiedades de los fliers (valores atípicos)
flierprops = dict(marker='o', markerfacecolor='red', markersize=5, linestyle='none')

#crear el grafico a detalle
plt.figure(figsize=(5,6))#ajustar el tamaño de grafico

#creando boxplot detallado con los datos ordenados
box = plt.boxplot(df_sorted['personas_alcanzadas'], patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

#personalizar colores de la caja
for patch in box['boxes']:
    patch.set_facecolor('lightblue')
#personalizar colore de los bigotes y medianas
for whisker in box ['whiskers']:
    whisker.set(color='black', linewidth=1.5)
#gorras(caps)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
#Mediana
for mean in box['means']:
    mean.set(marker='o', color='green', markersize=5)

#Etiquetas y titulo
plt.title('Distribucion de personas alcanzadas en anuncios', fontsize=16)
plt.ylabel('Personas', fontsize=16)
plt.grid(True, linestyle='--', alpha=1)

#Mostrar boxplot
plt.show()

#Identificar limites del boxplot
q1 = df_sorted['personas_alcanzadas'].quantile(0.25)
q3 = df_sorted['personas_alcanzadas'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

#filtrar anuncios con mas personas_alcanzadas por encima del limite superior
anuncios_outliers = df_sorted[df_sorted['personas_alcanzadas'] >upper_bound]

#mostrar los nombres de los anuncions que son outliers
print("anuncios con su valor fuera del rango (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'personas_alcanzadas']])