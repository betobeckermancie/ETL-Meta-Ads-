# creamos la base de datos en caso de que no exista
spark.sql("CREATE DATABASE IF NOT EXISTS db_pecsa_ads")

# leemos el csv
df = spark.read.csv("/mnt/processed/Ads_General_Por_Dia/anuncios_insights_general_por_dia_limpiado.csv", header=True, inferSchema=True)

# guardo el dataframe en la base de datos, se sobre escribe en caso de que exista
df.write.mode("overwrite").saveAsTable("db_pecsa_ads.meta_ads")

# verifico que la tabla se haya creado
spark.sql("SHOW TABLES IN db_pecsa_ads").show()

#SELECT * FROM db_pecsa_ads.meta_ads
