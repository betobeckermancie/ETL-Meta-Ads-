#cambiar el contenido de las columnas de spasnis a english
import pandas as pd

#cargar el archivo csv de origen en un dataframe
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_renombrado.csv")

#listar las columnas que vamos a remplazar
columns_to_replace=['conversion_mercado','calidad_mercado','tipo_compra']

#diccionario con los valores a remplazar y los nuevos valores
replacements = {
    'UNKNOWN': 'desconocido',
    'ABOVE_AVERAGE': 'arriba del promedio',
    'AVERAGE': 'promedio',
    'BELOW_AVERAGE_35': 'abajo del promedio',
    'BELOW_AVERAGE_20': 'abajo del promedio',
    'AUCTION':'subasta'

}

#remplazamos valores 'UNKNOWN' por 'desconocido'
df[columns_to_replace]=df[columns_to_replace].replace(replacements)

#guardar el dataframe en un nuevo archivo csv
df.to_csv("/dbfs/mnt/processed/anuncios_insights_modificado.csv", index=False)