#Esta combinación está enfocada en el rendimiento del anuncio basado 
#en métricas visuales. Permite observar si los anuncios que alcanzan
#más personas y tienen más visualizaciones de video también generan 
#un menor costo por clic y más contenido guardado
nombre_anuncio, personas_alcanzadas, costo_por_click_anuncio, 
vistas_video, contenido_guardado
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#cargar csv
columns_to_analyze=["nombre_anuncio", "personas_alcanzadas", "costo_por_click_anuncio","vistas_video","contenido_guardado"]

#agrupamos por nombre de anuncio y filtramos los 3 con mayores veces mostrados
top_3= df.groupby("nombre_anuncio", "personas_alcanzadas","costo_por_click_anuncio","vistas_video","contenido_guardado")
