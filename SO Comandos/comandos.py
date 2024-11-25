#ver los archivos que existen dentro de la ruta 
dbutils.fs.ls("/mnt/processed")

#borrar archivos expecificos dentro de una carpeta
dbutils.fs.rm("/mnt/processed/archivo_a_eliminar.csv", True)

#otra forma mismo resultado
file_path = "dbfs:/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"

try:
    dbutils.fs.rm(file_path, True)
    print("Archivo eliminado con éxito.")
except Exception as e:
    print(f"Error al intentar eliminar el archivo: {e}")

# Verificar si el archivo existe
file_path = "/dbfs/mnt/GoogleSheets/CSV's_Descargados/Combined_Data.csv"
exists = dbutils.fs.ls("/dbfs/mnt/GoogleSheets/CSV's_Descargados/")
file_found = any(file.name == "Combined_Data.csv" for file in exists)

print(f"El archivo existe: {file_found}")

#cambiar el nombre a un archivo
dbutils.fs.mv("dbfs:/mnt/processed/anuncios_insights05092024.csv", "dbfs:/mnt/processed/anuncios_insights05_09_2024.csv")
dbutils.fs.ls("/mnt/processed")


#revisar el contenido de cada columna
import pandas as pd

df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_clean05_09_2024.csv")

# Ver las columnas del DataFrame
display(df.columns)