#Esta combinación está enfocada en el rendimiento del anuncio basado 
#en métricas visuales. Permite observar si los anuncios que alcanzan
#más personas y tienen más visualizaciones de video también generan 
#un menor costo por clic y más contenido guardado

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#cargar csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columnas para analizar
columns_to_analyze=["nombre_anuncio", "personas_alcanzadas", "costo_por_click_anuncio","vistas_video","contenido_guardado"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3= df.groupby("nombre_anuncio")["veces_mostrado"].sum().nlargest(3).index

#filtramos df para dejar solo el top 3
df_filtrado = df[df["nombre_anuncio"].isin(top_3)]

#creamos el pairplot
plt.figure(figsize=(10, 6))
g=sns.pairplot(df_filtrado[columns_to_analyze],height=1.5, hue='nombre_anuncio', palette='bright')

#titulo el pairplot 
plt.suptitle("Relacion entre variables para los 3 anuncios con mayores numeros", y=1.18, fontsize=16)

#mover la leyenda arriba del grafico
g.legend.set_bbox_to_anchor((0.5,1.05))#ajuste posicion
g.legend.set_title("Top 3 Anuncios")

#mostrar grafico
plt.tight_layout()
plt.show()