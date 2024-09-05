import pandas as pd
import os

# agregar el token de largo plazo aquí
long_lived_token = ""

# Crear el directorio si no existe
directory = '/dbfs/mnt/Token_LargoPlazo'
if not os.path.exists(directory):
    os.makedirs(directory)

# Crear un DataFrame con el token
df_Token_LargoPlazo = pd.DataFrame({"access_token": [long_lived_token]})

# Guardar el DataFrame en un archivo CSV
df_Token_LargoPlazo.to_csv("/dbfs/mnt/Token_LargoPlazo/long_lived_token.csv", index=False)

