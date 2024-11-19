# Contenido del archivo JSON de credenciales (copia el contenido exacto del archivo aquí)
credentials_json = """
{
  "type": "service_account",
  "project_id": "tu-proyecto-id",
  "private_key_id": "tu-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\ntu-clave-privada\n-----END PRIVATE KEY-----\n",
  "client_email": "tu-cuenta@tu-proyecto-id.iam.gserviceaccount.com",
  "client_id": "tu-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tu-cuenta%40tu-proyecto-id.iam.gserviceaccount.com"
}
"""

# Especifica la ruta en DBFS donde deseas guardar el archivo
path = "/mnt/credentials/google_sheets_creds.json"

# Guarda el archivo JSON en DBFS
dbutils.fs.put(path, credentials_json, overwrite=True)

print(f"Archivo subido a {path}")
