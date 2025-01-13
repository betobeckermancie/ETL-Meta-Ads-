##convertir 'fecha_inicio' a date para eliminar los registros del 2024
import pandas as pd

# leer archivo csv
df = pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado_date.csv")

# convertir la columna 'fecha_inicio' a datetime
df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'])

# filtrar el dataframe para eliminar registros del 2024
df = df[df['fecha_inicio'].dt.year != 2024]

# guardar los cambios
df.to_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv", index=False)

# muestra los cambios
display(df)