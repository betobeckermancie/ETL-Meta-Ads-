#Esta combinación se centra en la interacción del usuario con el contenido visualizado en los anuncios.
#Like y reacciones_post representan interacciones directas, mientras que veces_mostrado 
#y vistas_video indican la exposición del contenido.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columnas para anlizar
columns_to_analyze =["nombre_anuncio", "like", "reacciones_post", "veces_mostrado","vistas_video"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3_anuncios = df.groupby("nombre_anuncio")["veces_mostrado"].sum().nlargest(3).index

#filtramos df para dejar solo el top 3
df_filtrado = df[df["nombre_anuncio"].isin(top_3_anuncios)]

#creamos el pairplot
plt.figure(figsize=(10,6))
g=sns.pairplot(df_filtrado[columns_to_analyze],height=1.5,hue='nombre_anuncio', palette='bright')

#titulo de cabecera
plt.suptitle("Relación entre variables para los 3 anuncios con mayores números", y=1.18, fontsize=16) 

#mover la leyenda arriba del grafico
g.legend.set_bbox_to_anchor((0.5,1.05)) #ajuste posicion
g.legend.set_title("Top 3 Anuncios")

#mostrar grafico
plt.tight_layout()
plt.show()