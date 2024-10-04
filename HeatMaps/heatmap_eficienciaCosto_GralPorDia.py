#Eficiencia del Costo
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#correlaciones 
#1 indica una correlacion positiva efectiva perfecta: a medida que una metrica aumenta,
#la otra tambien lo hace
#-1 indica una correlacion negatica perfecta: cuna una metrica aumenta, la otra disminuye
#0 indica que no hay correlacion


#carga csv 
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#seleccionar las columnas para analizar
columns_to_analyze = ["costo_por_resultado", "click_enlace_trafico", "costo_por_mil_impresiones","veces_mostrado","costo_por_click_anuncio","conversion_boton_msj"]

#creamos la matriz de correlacion entre las variables
correlation_matrix = df[columns_to_analyze].corr()

# crear el heatmap con seaborn
plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", linewidths=0.5)

#agregar etiquetas y titulo 
plt.title("Heatmap de correlación entre métricas publicitarias", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)

#mostrar el grafico
plt.tight_layout()
plt.show()