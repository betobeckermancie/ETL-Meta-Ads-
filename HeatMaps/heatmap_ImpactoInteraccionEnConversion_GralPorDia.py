#Impacto de las Interacciones en la Conversión
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#correlaciones 
#1 indica una correlacion positiva efectiva perfecta: a medida que una metrica aumenta,
#la otra tambien lo hace
#-1 indica una correlacion negatica perfecta: cuna una metrica aumenta, la otra disminuye
#0 indica que no hay correlacion

#cargar el archivo csv 
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#seleccionar las columnas para analizarlas
columns_to_analyze = ["click_enlace_trafico", "conversion_boton_msj", "reacciones_post","comentarios","contenido_guardado"]

# Verificar si hay valores nulos en la columna 'contenido_guardado' y llenarlos con 0 (podemos cambiar el valor al que queramos)
df['contenido_guardado'].fillna(0, inplace=True)

#creamos mariz de correlacion entre las variables
corelation_matrix = df[columns_to_analyze].corr()

#crear el heatmp con seaborn
plt.figure(figsize=(10,6))
sns.heatmap(corelation_matrix, annot=True, cmap="YlGnBu", linewidths=0.5)

#agregar etiqutadas y titulo
plt.title("Heatmap de correlación entre métricas publicitarias", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

#mostrar el grafico
plt.tight_layout()
plt.show()

