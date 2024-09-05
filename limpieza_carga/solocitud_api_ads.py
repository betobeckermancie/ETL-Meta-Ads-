#codigo para guardar todos los insights necesarios para el analisis de datos de SOLO los anuncios
import requests
import pandas as pd
import os

# Leer el token desde el archivo CSV previamente guardado
df_TokenLargoPlazo = pd.read_csv("/dbfs/mnt/Token_LargoPlazo/long_lived_token.csv")
access_token = df_TokenLargoPlazo["access_token"].iloc[0]

# Reemplaza este valor con tu ad_account_id (ID de la cuenta publicitaria de Meta)
ad_account_id = "1952584805183463"

# Crear el directorio '/dbfs:/mnt/processed' si no existe
processed_dir = '/dbfs/mnt/processed'
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# Función para obtener todos los conjuntos de anuncios de todas las campañas
def obtener_conjuntos_anunciosMeta(access_token, ad_account_id):
    url = f"https://graph.facebook.com/v13.0/act_{ad_account_id}/adsets"
    params = {
        "access_token": access_token,
        "fields": "id,name,status"  # Especifica las columnas que deseas obtener
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        df_conjuntosMeta = pd.DataFrame(data)
        return df_conjuntosMeta
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Función para obtener el alcance de un anuncio mediante el endpoint de insights
def obtener_alcance_anuncio(access_token, ad_id):
    url = f"https://graph.facebook.com/v13.0/{ad_id}/insights"
    params = {
        "access_token": access_token,
        "fields": "ad_id,ad_name,adset_name,campaign_name,date_start,date_stop,reach,impressions,frequency,spend,clicks,cost_per_ad_click,inline_link_clicks,conversion_rate_ranking,cpc,cpp,cpm,actions,ad_click_actions,quality_ranking,conversions,buying_type",  # Especifica las métricas que deseas obtener
        "level": "ad"  # Nivel de la métrica, en este caso es a nivel de anuncio
    }

    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        df_insights = pd.DataFrame(data)
        return df_insights
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Obtener todos los conjuntos de anuncios
df_conjuntos = obtener_conjuntos_anunciosMeta(access_token, ad_account_id)

if df_conjuntos is not None:
    all_insights = []
    # Obtener y guardar el alcance y otras métricas para cada anuncio en los conjuntos de anuncios
    for adset_id in df_conjuntos['id']:
        url = f"https://graph.facebook.com/v13.0/{adset_id}/ads"
        params = {
            "access_token": access_token,
            "fields": "id,name"  # Obtener solo los IDs de los anuncios
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            ads_data = response.json()['data']
            for ad in ads_data:
                ad_id = ad['id']
                df_anuncio_insights = obtener_alcance_anuncio(access_token, ad_id)
                if df_anuncio_insights is not None:
                    all_insights.append(df_anuncio_insights)

    # Unir todos los DataFrames de insights en uno solo
    if all_insights:
        df_all_insights = pd.concat(all_insights, ignore_index=True)
        # Guardar todos los insights en un solo CSV
        df_all_insights.to_csv(f"{processed_dir}/anuncios_insightsTEST.csv", index=False)
        print("Todos los insights de los anuncios guardados exitosamente.")
    else:
        print("No se encontraron insights de anuncios.")
else:
    print("No se encontraron conjuntos de anuncios o limite de solicitud excedido.")