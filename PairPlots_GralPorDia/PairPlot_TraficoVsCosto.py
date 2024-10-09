#El foco de esta combinación está en analizar el tráfico generado por los anuncios 
# y su costo por mil impresiones. Te permitirá observar la relación entre el tráfico 
# generado, la interacción en las publicaciones y la frecuencia con la que se muestran
# los anuncios.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#cargar el csv
df =pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columns para analizar
columns_to_analyze = ["nombre_anuncio","click_enlace_trafico","costo_por_mil_impresiones"," interaccion_post","promedio_frecuencia"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3 = df.groupby("nombre_anuncio")["veces_mostrado"].sum().nlargest(3).index

#filtramos df para dear solo el top 3
df_filtrado = df[df["nombre_anuncio"].isin(top_3)]

#cremos el pairplot
plt.figure(figsize=(10, 6))
g=sns.pairplot(df_filtrado[columns_to_analyze],height=1.5,hue='nombre_anuncio',palette='bright')

#titulo de cabecera
plt.suptitle("Relación entre variables para los 3 anuncios con mayores números", y=1.18, fontsize=16)

#mover la leyenda arriba del grafico
g.legend.set_bbox_to_anchor((0.5,1.05))#ajuste
g.legend.set_title("Top 3 anuncios")

#mostrar grafico
plt.tight_layout()
plt.show()