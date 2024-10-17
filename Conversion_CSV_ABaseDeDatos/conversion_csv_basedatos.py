from datetime import datetime

#leo archivo csv desde el sistema de archivos de databricks (DFBS)
df = spark.read.csv("dbfs:/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv",header=True, inferSchema=True)

#crear una vista temporal para consultar datos usando sql en databricks
df.createOrReplaceTempView("meta_ads_limpiado_tabla")


#obtener fecha actual en formato dd_mm_yyyy
fecha_actual =datetime.now().strftime("%d_%m_%Y")

#crear el nombre dinamico del archivo o tabla
nombre_tabla=f"meta_ads{fecha_actual}"

#guardar tabla de forma permanente en databricks para acceder con powerbi
df.write.form("delta").saveAsTable("meta_ads")