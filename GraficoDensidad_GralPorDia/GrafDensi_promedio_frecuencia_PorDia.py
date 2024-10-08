import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#cargar el csv
df=pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#variable para analizar
variable_analizar = 'promedio_frecuencia'

#creo grafica de densidad
plt.figure(figsize=(10, 6))
sns.kdeplot(df[variable_analizar], fill=True)

#etiquetas y titulo de la grafica 
plt.title(f"Densidad de {variable_analizar}")
plt.xlabel("Valor")
plt.ylabel("Densidad")

#etiquetas y titulo de la grafica
plt.xticks(range(0, int(df[variable_analizar].max())+100,100))
plt.tight_layout()
plt.show()