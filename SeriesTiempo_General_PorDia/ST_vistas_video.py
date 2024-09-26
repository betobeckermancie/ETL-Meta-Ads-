import panda as pd
import matplotlib as plt

#cargamos el archivo cvs 
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#confirmar que la columna fecha_inicio sea tipo datetime
df['fecha_inicio'] = pd.to_datetime(df["fecha_inicio"])

#establecer la columna 'fecha_inicio' para el indice para aplicar la time serie
df.set_index("fecha_inicio", inplace=True)

#se usa para hacer dinamico el titulo
variable_analizar = "reacciones_post" #cambiar cuando sea necesario

#seleccionar las columnas para analizar
df_time_series = df[variable_analizar]

#resamplear los datos segun sea necesario analizar ya sea Dia 'D'
#semana 'W' o año 'Y'
df_resampled = df_time_series.resample("D").sum

#se usa para hacer dinamicas las etiquetas
if df_time_series.resample("D"):
    fecha = "Dia"
elif df_time_series.resample("W"):
    fecha = "Semana"
elif df_time_series.resampe("M"):
    fecha = "Mes"
else:
    fecha = "Anual"

#Graficar la serie de tiempo 
plt.figure(figsize=(10,6))
df_resampled.plot(title = f"Serie de tiempo de {variable_analizar} por dia", color="blue")

#agregar etiquetas a grafica
plt.xlabel(f"Analisis {fecha}")
plt.ylabel("Total")
plt.grid(True)

#Mostrar la grafica 
plt.tight_layout()
plt.show()