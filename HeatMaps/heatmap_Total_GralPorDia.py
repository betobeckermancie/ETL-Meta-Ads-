import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#correlaciones 
#1 indica una correlacion positiva efectiva perfecta: a medida que una metrica aumenta,
#la otra tambien lo hace
#-1 indica una correlacion negatica perfecta: cuna una metrica aumenta, la otra disminuye
#0 indica que no hay correlacion



# Cargar el archivo CSV
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

# Seleccionar solo las columnas numéricas
df_numeric = df.select_dtypes(include='number')

# Excluir una columna específica (por ejemplo, 'clicks_en_anuncio')
df_numeric = df_numeric.drop(columns=['clicks_en_anuncio'])

# Calcular la correlación
correlation_matrix = df_numeric.corr()

# Ajustar el tamaño de la figura para evitar que las etiquetas se amontonen
plt.figure(figsize=(12, 10))

# Crear el heatmap con rotación de las etiquetas para mayor claridad
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', 
            linewidths=0.5, annot_kws={"size": 8})  # Puedes ajustar el tamaño del texto de las anotaciones

# Rotar las etiquetas del eje X y Y para que no se superpongan
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)

# Añadir el título
plt.title("Heatmap de correlación (sin 'clicks_en_anuncio')", fontsize=14)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
