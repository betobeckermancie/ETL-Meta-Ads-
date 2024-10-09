#Esta combinación te permite ver cómo los clics en los anuncios y las visualizaciones de videos están correlacionados con las conversiones 
#en botones de mensaje y el contenido guardado. Es útil para analizar el comportamiento del usuario a partir de interacciones visuales 
#y su impacto en las conversiones.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columnas para anlizar
columns_to_analyze =["nombre_anuncio", "clicks_en_anuncio", "vistas_video", "conversion_boton_msj","contenido_guardado"]

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