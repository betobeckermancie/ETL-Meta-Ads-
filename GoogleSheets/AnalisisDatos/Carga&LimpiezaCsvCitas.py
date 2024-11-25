#archivo para cargar y verificar la coneccion las las hojas de google shets
#se tiene que habilitar el uso de la api google drive

#libreria a instalar
#%pip install gspread google-auth
#%pip install gspread oauth2client

#reiniciar python para que detecte librerias
#dbutils.library.restartPython()

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuracion de credenciales / url de las apis
scope=[
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

json_creds_path = "/dbfs/mnt/GoogleSheets/Credenciales/GoogleSheets_Credenciales.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name
(json_creds_path, scope)
client = gspread.authorize(credentials)

#Listar hojas de calculo a las que tengo permiso(para eso hay que compartir el correo
#de la cuenta que se esta usando en la api de google y darle permisos editor)
spreadsheets= client.openall()
print("Conexion extiosa. Hojas de calculo con acceso:")
for sheet in spreadsheets:
    print(f"- {sheet.title}")