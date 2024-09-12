import matplotlib.pyplot as plt
import pandas as pd

# Cargar el csv para analizar
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Agrupar los anuncios por nombre y sumar las interacciones
df_grouped = df.groupby('nombre_anuncio', as_index=False).sum(numeric_only=True)

# Ordenar los anuncios de mayor a menor por la columna 'msjs_respondidos_por_pecsa_antes_de_7Dias  '
df_sorted = df_grouped.sort_values(by='msjs_respondidos_por_pecsa_antes_de_7Dias ', ascending=False)

# Configurar las propiedades de los fliers (valores atípicos)
flierprops = dict(marker='o', markerfacecolor='red', markersize=5, linestyle='none')

# Crear el gráfico a detalle
plt.figure(figsize=(5,6))  # Ajustar el tamaño del gráfico

# Creando boxplot detallado con los datos agrupados
box = plt.boxplot(df_sorted['msjs_respondidos_por_pecsa_antes_de_7Dias '], patch_artist=True, notch=True, vert=True, showmeans=True, flierprops=flierprops)

# Personalizar colores de la caja
for patch in box['boxes']:
    patch.set_facecolor('lightblue')
# Personalizar colores de los bigotes y medianas
for whisker in box['whiskers']:
    whisker.set(color='black', linewidth=1.5)
# Gorras
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
# Mediana
for mean in box['means']:
    mean.set(marker='o', color='green', markersize=5)

# Etiquetas y título
plt.title('Distribución de msj respondidos por pecsa antes de los 7 dias', fontsize=16)
plt.ylabel('Cantidad', fontsize=16)
plt.grid(True, linestyle='--', alpha=1)

# Ajustar el rango del eje 'Y' y los ticks
#plt.ylim(0, df_grouped['msjs_respondidos_por_pecsa_antes_de_7Dias '].max()+500)  # Ajustar el límite superior del eje Y
#plt.yticks(range(0, int(df_grouped['msjs_respondidos_por_pecsa_antes_de_7Dias  '].max())+1000, 1000))  # Configurar los ticks de 1000 en 1000

# Mostrar gráfico
plt.show()

# Identificar límites del boxplot
q1 = df_sorted['msjs_respondidos_por_pecsa_antes_de_7Dias '].quantile(0.25)
q3 = df_sorted['msjs_respondidos_por_pecsa_antes_de_7Dias '].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filtrar anuncios con más msjs_respondidos_por_pecsa_antes_de_7Dias   por encima del límite superior
anuncios_outliers = df_sorted[df_sorted['msjs_respondidos_por_pecsa_antes_de_7Dias '] > upper_bound]

# Mostrar los nombres de los anuncios que son outliers
print("Anuncios con su valor fuera del rango (outliers):")
print(anuncios_outliers[['nombre_anuncio', 'msjs_respondidos_por_pecsa_antes_de_7Dias ']])