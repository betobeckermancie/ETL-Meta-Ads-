# Crear la base de datos en caso de que no exista
spark.sql("CREATE DATABASE IF NOT EXISTS db_pecsa_ads")

# Eliminar la tabla si ya existe
spark.sql("DROP TABLE IF EXISTS db_pecsa_ads.meta_ads")

# Leer el archivo CSV
df = spark.read.csv("/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv", header=True, inferSchema=True)

# Escribir el DataFrame como una nueva tabla
df.write.mode("overwrite").saveAsTable("db_pecsa_ads.meta_ads")

# Verificar que la tabla se haya creado
spark.sql("SHOW TABLES IN db_pecsa_ads").show()


#%sql
#SELECT * FROM db_pecsa_ads.meta_ads