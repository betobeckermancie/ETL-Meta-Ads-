import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# varible para analizar/se cambia 
variable_analizar = "conversion_primer_respuesta"

# se agrupa por el nombre del anuncio para que no se repita
df_grouped = df.groupby('nombre_anuncio')[variable_analizar].sum()

#ordena la variable y obtiene los 5 con mayor numero
top_5_ads = df_grouped.nlargest(5)

#convertimos el resultado en un dataframe para un formato tabla
top5ads_df = top_5_ads.reset_index()
top5ads_df.columns = ["nombe_anuncio", variable_analizar]

#imprimimos el top 5 con nombre y cantidad en fomato tabla
print("Top 5 Ads con Mayor numero de" ,variable_analizar)
print(top5ads_df.to_string(index=False))

# Creamos grafico de barras
plt.figure(figsize=(10, 6))
top_5_ads.plot(kind='bar', color="#FF6262")

# etiquetas y titulo a las graficas
plt.title(f"Top 5 Anuncios con Mayor Número de {variable_analizar}", fontsize=16)
plt.xlabel('Nombre de Anuncio',fontsize=12)
plt.ylabel(f"{variable_analizar}", fontsize=12)
plt.xticks(rotation=45, ha="right")

# mostramos el grafico
plt.tight_layout()
plt.show()