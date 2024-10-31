import requests
import pandas as pd

# Variables necesarias
app_id = ""  # ID de tu aplicación de Facebook
app_secret = ""  #Clave Secreta de tu aplicación
short_lived_token = ""  # Token de acceso de corto plazo

# URL para intercambiar el token de corto plazo por uno de largo plazo
url = f"https://graph.facebook.com/v13.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_lived_token}"

# Realizar la solicitud
response = requests.get(url)

# Verificar el resultado
if response.status_code == 200:
    # Extraer el token de largo plazo del resultado de la API
    long_lived_token = response.json().get("access_token")
    print("Nuevo Token de Largo Plazo:", long_lived_token)
    
    # Guardar el token de largo plazo en un archivo CSV
    df_Token_LargoPlazo = pd.DataFrame({"access_token": [long_lived_token]})
    df_Token_LargoPlazo.to_csv("/dbfs/mnt/Token_LargoPlazo/long_lived_token.csv", index=False)
    print("Token de Largo Plazo guardado exitosamente.")
else:
    # Mostrar el error si ocurre
    print("Error al intentar renovar el token:", response.text)