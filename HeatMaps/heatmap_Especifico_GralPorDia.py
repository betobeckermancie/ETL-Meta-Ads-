import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Seleccionar las columnas que te interesen analizar para el heatmap
# Especificar las columnas numéricas que quieres comparar
columns_to_analyze = ['clicks_en_anuncio', 'costo_por_click_anuncio', 'click_enlace_trafico', 'conversion_boton_msj']

# Crear una matriz de correlación entre estas variables
correlation_matrix = df[columns_to_analyze].corr()

# Crear el heatmap con Seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", linewidths=0.5)

# Agregar etiquetas y título
plt.title('Heatmap de correlación entre métricas publicitarias', fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
