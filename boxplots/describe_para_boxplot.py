#Si no existe valores en el costo_por_mil_impresiones mayores al upper_bound no existiran outliers

df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv")

#revisar que hay outliers en el dataset
print(df['costo_por_mil_impresiones'].describe())
print(df['costo_por_mil_impresiones'].isnull().sum())  # Verificar si hay valores nulos
print(df['costo_por_mil_impresiones'].unique())  # Ver valores únicos en la columna

print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Máximo valor en costo_por_mil_impresiones: {df['costo_por_mil_impresiones'].max()}")


# Ordenar el DataFrame por la columna 'costo_por_mil_impresiones' de mayor a menor
df_ordenado = df.sort_values(by='costo_por_mil_impresiones', ascending=False)

# Mostrar los anuncios con los valores más altos en 'costo_por_mil_impresiones'
print(df_ordenado[['nombre_anuncio', 'costo_por_mil_impresiones']])