#eficiencia de los clicks en los ads
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#correlaciones 
#1 indica una correlacion positiva efectiva perfecta: a medida que una metrica aumenta,
#la otra tambien lo hace
#-1 indica una correlacion negatica perfecta: cuna una metrica aumenta, la otra disminuye
#0 indica que no hay correlacion


# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Seleccionar las columnas que te interesen analizar para el heatmap
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
