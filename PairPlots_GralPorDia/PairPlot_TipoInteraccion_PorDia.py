#Se enfoca en la interacción directa del usuario con el anuncio. Con estas variables,
#puedes evaluar qué tipo de interacción está recibiendo cada anuncio y cómo las 
#reacciones, likes y comentarios están correlacionados entre sí. 
#Es útil para comprender qué anuncios fomentan más interacciones sociales.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#cargar el csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columnas para analizar
columns_to_analyze = ["nombre_anuncio", "interaccion_post", "reacciones_post","comentarios"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3_anuncios = df.groupby("nombre_anuncio")["veces_mostrado"].sum().nlargest(3).index

#filtramos df para dejar solo el top 3
df_filtrado = df[df["nombre_anuncio"].isin(top_3_anuncios)]

#creamos el pairplot
plt.figure(figsize=(10, 6))
g=sns.pairplot(df_filtrado[columns_to_analyze], height=1.5,hue='nombre_anuncio',palette="bright")

#titulo de cabecera
plt.suptitle("Relacion entre variables para los 3 anuncios con mayores numeros", y=1.18, fontsize=16)

#mover la leyenda arriba del grafico
g.legend.set_bbox_to_anchor((0.5,1.05))#ajustar posicion
g.legend.set_title("Top 3 anuncios")

#mostrar grafico
plt.tight_layout()
plt.show()