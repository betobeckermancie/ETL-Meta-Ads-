#util para saber si estamos pagando mas por clics en ads con menos interaccion o viceversa
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Seleccionar las columnas que deseas analizar
columns_to_analyze = ['clicks_en_anuncio', 'costo_por_click_anuncio', 'click_enlace_trafico']

# Crear un DataFrame nuevo solo con las columnas seleccionadas
df_to_plot = df[columns_to_analyze]

# Crear un boxplot múltiple
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_to_plot)

# Agregar etiquetas y título
plt.title("Boxplot múltiple de interacciones y costo", fontsize=16)
plt.ylabel("Valor")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
