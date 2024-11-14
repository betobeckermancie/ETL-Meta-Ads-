import requests
import pandas as pd
import os
import time  # Importamos time para pausar el script con sleep

# Leer el token desde el archivo CSV previamente guardado
df_TokenLargoPlazo = pd.read_csv("/dbfs/mnt/Token_LargoPlazo/long_lived_token.csv")
access_token = df_TokenLargoPlazo["access_token"].iloc[0]

# ID de la cuenta publicitaria de Meta
ad_account_id = "1952584805183463"

# Crear un directorio para guardar los datos si no existe
processed_dir = '/dbfs/mnt/processed/Ads_GralTotal'
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# Función para obtener todas las campañas de una cuenta publicitaria con paginación
def obtener_campanasMeta(access_token, ad_account_id):
    """
    Obtiene todas las campañas asociadas a una cuenta publicitaria, usando paginación para manejar resultados grandes.
    """
    url = f"https://graph.facebook.com/v13.0/act_{ad_account_id}/campaigns"
    params = {
        "access_token": access_token,
        "fields": "id,name,status",  # Campos específicos a recuperar
        "limit": 25  # Límite por página
    }
    all_campaigns = []  # Lista para acumular todas las campañas
    while url:  # Mientras exista una URL para la siguiente página
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_campaigns.extend(data['data'])
            url = data.get('paging', {}).get('next')  # Obtener la siguiente URL
        else:
            print(f"Error al obtener campañas {response.status_code}: {response.text}")
            break
    return pd.DataFrame(all_campaigns) if all_campaigns else None

# Función para obtener conjuntos de anuncios de una campaña con paginación
def obtener_conjuntos_anunciosMeta(access_token, campaign_id):
    """
    Obtiene todos los conjuntos de anuncios para una campaña específica, usando paginación.
    """
    url = f"https://graph.facebook.com/v13.0/{campaign_id}/adsets"
    params = {
        "access_token": access_token,
        "fields": "id,name,status,effective_status",
        "limit": 25  # Límite por página
    }
    all_adsets = []  # Lista para acumular todos los conjuntos de anuncios
    while url:  # Mientras exista una URL para la siguiente página
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_adsets.extend(data['data'])
            url = data.get('paging', {}).get('next')  # Obtener la siguiente URL
        else:
            print(f"Error al obtener conjuntos de anuncios {response.status_code}: {response.text}")
            break
    return pd.DataFrame(all_adsets) if all_adsets else None

# Función para obtener anuncios de un conjunto de anuncios con paginación
def obtener_anunciosMeta(access_token, adset_id):
    """
    Obtiene todos los anuncios asociados a un conjunto de anuncios, usando paginación.
    """
    url = f"https://graph.facebook.com/v13.0/{adset_id}/ads"
    params = {
        "access_token": access_token,
        "fields": "id,name,effective_status",
        "limit": 25  # Límite por página
    }
    all_ads = []  # Lista para acumular todos los anuncios
    while url:  # Mientras exista una URL para la siguiente página
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_ads.extend(data['data'])
            url = data.get('paging', {}).get('next')  # Obtener la siguiente URL
        else:
            print(f"Error al obtener anuncios {response.status_code}: {response.text}")
            break
    return pd.DataFrame(all_ads) if all_ads else None

# Función para obtener métricas (insights) de un anuncio
def obtener_alcance_anuncio(access_token, ad_id):
    """
    Recupera las métricas (insights) de un anuncio específico.
    """
    url = f"https://graph.facebook.com/v13.0/{ad_id}/insights"
    params = {
        "access_token": access_token,
        "fields": "ad_id,ad_name,adset_name,campaign_name,date_start,date_stop,reach,impressions,frequency,spend,clicks,cost_per_ad_click,inline_link_clicks,conversion_rate_ranking,cpc,cpp,cpm,actions,ad_click_actions,quality_ranking,conversions,buying_type",  # Métricas solicitadas
        "level": "ad"  # Nivel de la métrica (anuncio)
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        return pd.DataFrame(data) if data else None
    else:
        print(f"Error al obtener insights del anuncio {response.status_code}: {response.text}")
        return None

# Flujo principal
df_campanas = obtener_campanasMeta(access_token, ad_account_id)  # Obtener todas las campañas
if df_campanas is not None:
    all_insights = []  # Lista para acumular los insights de todos los anuncios
    for i, campana in df_campanas.iterrows():
        print(f"Procesando campaña {i + 1} de {len(df_campanas)}: {campana['name']}")
        campaign_id = campana['id']
        df_conjuntos = obtener_conjuntos_anunciosMeta(access_token, campaign_id)
        
        # Verificar si excede el límite de conjuntos de anuncios
        if df_conjuntos is not None:
            if len(df_conjuntos) > 13:
                print("Se alcanzaron más de 14 conjuntos de anuncios. Pausando 5 minutos...")
                time.sleep(300)

            for j, conjunto in df_conjuntos.iterrows():
                print(f"  Procesando conjunto de anuncios {j + 1} de {len(df_conjuntos)}: {conjunto['name']}")
                adset_id = conjunto['id']
                df_anuncios = obtener_anunciosMeta(access_token, adset_id)
                
                # Verificar si excede el límite de anuncios
                if df_anuncios is not None:
                    if len(df_anuncios) > 33:
                        print("Se alcanzaron más de 34 anuncios. Pausando 5 minutos...")
                        time.sleep(300)

                    for k, anuncio in df_anuncios.iterrows():
                        print(f"    Procesando anuncio {k + 1} de {len(df_anuncios)}: {anuncio['name']}")
                        ad_id = anuncio['id']
                        df_anuncio_insights = obtener_alcance_anuncio(access_token, ad_id)
                        if df_anuncio_insights is not None:
                            all_insights.append(df_anuncio_insights)

        # Pausa adicional por cada campaña
        print("Esperando 5 minutos antes de procesar la siguiente campaña...")
        time.sleep(300)

    # Guardar todos los insights en un archivo CSV
    if all_insights:
        df_all_insights = pd.concat(all_insights, ignore_index=True)
        df_all_insights.to_csv(f"{processed_dir}/ads_GralTotal.csv", index=False)
        print("Todos los insights de los anuncios guardados exitosamente.")
    else:
        print("No se encontraron insights para los anuncios.")
else:
    print("No se encontraron campañas en la cuenta publicitaria.")

# Verificar archivos creados
dbutils.fs.ls("/mnt/processed/Ads_GralTotal")