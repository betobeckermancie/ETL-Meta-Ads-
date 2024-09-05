#ver los archivos que existen dentro de la ruta 
dbutils.fs.ls("/mnt/processed")

#borrar archivos expecificos dentro de una carpeta
dbutils.fs.rm("/mnt/processed/archivo_a_eliminar.csv")

#cambiar el nombre a un archivo
dbutils.fs.mv("dbfs:/mnt/processed/anuncios_insights05092024.csv", "dbfs:/mnt/processed/anuncios_insights05_09_2024.csv")
dbutils.fs.ls("/mnt/processed")