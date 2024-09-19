import pandas as pd
import matplotlib.pyplot as plt

#cargamos el archivo csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#verificamos que la columna fecha_inicio este en formato fecha
df['fecha_inicio']= pd.to_datetime(df['fecha_inicio'])

#extraemos el dia de la semana 
df['day_of_week'] = df['fecha_inicio'].dt.dayofweek

#Mapear/asignar los valores numericos a los nombres de los dias
dias_semana = {0: 'Lunes', 1:'Martes', 2:"Miercoles", 3:"Jueves",4:"Viernes",5:"Sabado",6:"Domingo"}
df['day_of_week']=df['day_of_week'].map(dias_semana)

#columna dinamica para que cuando cambiemos la variable a analizar se cambie el titulo
columna_a_analizar='conversion_primer_respuesta'#aqui cambiare la variable a analizar}

#Agrupare el dia de la semana y sumare las cantiades
df_grouped = df.groupby('day_of_week')[columna_a_analizar].sum()

#Ordeno los dias de la semana en orden correcto
df_grouped = df_grouped.reindex(["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])

#crear el grafico de barras 
plt.figure(figsize=(10,8))
df_grouped.plot(kind='bar', color='skyblue')

#agregar etiquetas y titulo dinamico
plt.title(f'Total de {columna_a_analizar} por Dia de la Semana')#titulo dinamico
plt.ylabel(f'Cantidad')# etiqueta dinamica para el eje Y

#Mostrar el grafico
plt.tight_layout()
plt.show()