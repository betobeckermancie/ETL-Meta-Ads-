import pandas as pd
import matplotlib.pyplot as plt

#cargamos el archivo csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#confirmar que la columna fecha_inicio sea tipo datatime
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])

#establezco la columna 'fecha_inicio' como el indice del dataframe para aplicar la time_serie
df.set_index("fecha_inicio", inplace=True)

#establezco la variable a analizar para usarlo de forma dinamica
variable_analizar = "conversion_boton_msj"#cambiar cuando sea necesario

#seleccionar las columnas para analizar
df_time_series =df[variable_analizar]

#remplazar los datos segun sea necesario analizar ya sea
# dia 'D', semana 'W', mes 'M' o año 'Y'.
df_resampled = df_time_series.resample('D').sum()

#se usa para hacer dinamicas las etiquetas
if df_time_series.resample('D'):
    fecha = "Dia"
elif df_time_series.resample('W'):
    fecha = "Semana"
elif df_time_series.resample('M'):
    fecha = "Mes"
else:
    fecha = "Anual"

    
# Graficar la serie de tiempo
plt.figure(figsize=(10,6))
df_resampled.plot(title=f"Serie de tiempo de {variable_analizar} por dia", color='blue')

#agregar etiquetas a grafica
plt.xlabel(f"Analis  {fecha}")
plt.ylabel("Total")
plt.grid(True)

#mostrar la grafica
plt.tight_layout()
plt.show()