#Esta combinación ayuda a analizar cómo el número de veces que se
#muestra el anuncio (exposición) y el gasto están relacionados con
#los clics y las conversiones en botón de mensaje. 
#Te permite identificar qué anuncios generan más conversiones 
#en relación con la cantidad de veces mostradas y el presupuesto
#gastado.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#cargar csv
# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#columnas para analizar
columns_to_analyze=["nombre_anuncio", "clicks_en_anuncio", "conversion_boton_msj","gasto"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3_anuncios = df.groupby("nombre_anuncio")['veces_mostrado'].sum().nlargest(3).index

#filtramos df para dejar solo el top 3
df_filtrado =df[df['nombre_anuncio'].isin(top_3_anuncios)]

#creamos el pairplot
plt.figure(figsize=(10, 6))
g=sns.pairplot(df_filtrado[columns_to_analyze], height=1.5,hue='nombre_anuncio', palette='bright')

#titulo de cabecera
plt.suptitle("Relacion entre las variables para los 3 anuncios con mayores numeros", y=1.18,fontsize=16)

#mover la leyenda arriba del grafico
g.legend.set_bbox_to_anchor((0.5,1.5))#ajuste posicion
g.legend.set_title("Top 3 anuncios")

#mostrar grafico
plt.tight_layout()
plt.show()