import pandas as pd
import matplotlib.pyplot as plt

#cargamos el archivo csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#establecer la columna 'fecha_inicio' como indice para aplicar l la time serie
df['fecha_inicio'] = pd.to_datetime(df["fecha_inicio"])

#establecer la columna 'fecha_inicio' como indice para aplicar a la time serie
df.set_index("fecha_inicio", inplace=True)

#se usa para hacer dinamico el titulo
variable_analizar = "comentarios" #cambiar cuando sea necesario

#seleccionamos las columnas para analizar
df_time_series = df[variable_analizar]

#resamplear los datos segun sea necesario analizar Dia 'D',
#semana 'W' o año 'Y'
df_resampled = df_time_series.resample("D").sum()

#se usa para hacer dinamicas las etiquetas
if df_time_series.resample("D"):
    fecha="Dia"
elif df_time_series.resample("W"):
    fecha="Semana"
elif df_time_series.resample("M"):
    fecha="Mes"
else:
    fecha="Anual"

#Graficar la serie de tiempo
plt.figure(figsize=(10, 8))
df_resampled.plot(title=f"Serie de tiempo de {variable_analizar} por dia", color="blue")

#agregar etiquetas para la grafica
plt.xlabel(f"Analisi de {fecha}")
plt.ylabel("Total")
plt.grid(True)

#mostrar la grafica 
plt.tight_layout()
plt.show()
