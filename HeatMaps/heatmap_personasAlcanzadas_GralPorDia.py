#Relación entre el Alcance y las Interacciones
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#correlaciones 
#1 indica una correlacion positiva efectiva perfecta: a medida que una metrica aumenta,
#la otra tambien lo hace
#-1 indica una correlacion negatica perfecta: cuna una metrica aumenta, la otra disminuye
#0 indica que no hay correlacion

#cargar el csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#seleccionar las columnas para analizar
columns_to_analyze = ["personas_alcanzadas", "veces_mostrado", "vistas_video","interaccion_post"]

#crear una matriz de correlacion entre estas variables
correlation_matrix = df[columns_to_analyze].corr()

#crear el heatmap con Seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", linewidths=0.5)

#agregar etiquetas y titulo
plt.title("Heatmap de correlación entre el Alcance y las Interacciones", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

#Mostrar
plt.tight_layout()
plt.show()