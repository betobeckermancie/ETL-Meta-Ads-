#ver los archivos que existen dentro de la ruta 
dbutils.fs.ls("/mnt/processed")

#borrar archivos expecificos dentro de una carpeta
dbutils.fs.rm("/mnt/processed/archivo_a_eliminar.csv")

#cambiar el nombre a un archivo
dbutils.fs.mv("dbfs:/mnt/processed/anuncios_insights05092024.csv", "dbfs:/mnt/processed/anuncios_insights05_09_2024.csv")
dbutils.fs.ls("/mnt/processed")


#revisar el contenido de cada columna
import pandas as pd

df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Ver las columnas del DataFrame
display(df.columns)