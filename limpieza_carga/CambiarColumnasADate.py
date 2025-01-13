import pandas as pd
df =pd.read_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv")

#se convierte la columna en tipo de dato datetime pero solo se guarda la fecha
df['fecha_inicio']= pd.to_datetime(df['fecha_inicio']).dt.date
df['fecha_finalizacion'] = pd.to_datetime(df["fecha_finalizacion"]).dt.date

#se guarda en un dataframe
df.to_csv("/dbfs/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado_date.csv", index=False)

#se muestran los cambios
display(df)