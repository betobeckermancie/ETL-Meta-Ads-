#cambiar columnas de csv con mas detalles en spanish
import pandas as pd

#leer el csv desde la ruta especificada
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insights_expanded_numeric.csv")

#diccionario con los cambios de nombres en columnas/agregar nombres columnas a cambiar por nuevos nombres
new_column_names ={
    'ad_id': 'id_anuncio',
    'ad_name': 'nombre_anuncio',
    'campaign_name': 'nombre_campana',
    'date_start': 'fecha_inicio',
    'date_stop': 'fecha_finalizacion',
    'reach': 'personas_alcanzadas',
    'impressions': 'veces_mostrado',
    'frequency': 'promedio_frecuencia',
    'spend': 'gasto',
    'clicks': 'clicks_en_anuncio',
    'inline_link_clicks': 'click_enlace_trafico',
    'conversion_rate_ranking': 'conversion_mercado',
    'cpc': 'costo_por_click_anuncio',
    'cpp': 'costo_por_resultado',
    'cpm': 'costo_por_mil_impresiones',
    'quality_ranking': 'calidad_mercado',
    'buying_type': 'tipo_compra',
    'onsite_conversion.total_messaging_connection': 'conversion_boton_msj',
    'onsite_conversion.messaging_first_reply': 'conversion_primer_respuesta',
    'post_engagement': 'interaccion_post',
    'page_engagement': 'interaccion_page',
    'onsite_conversion.messaging_user_depth_2_message_send': '2do_msj_cliente',
    'onsite_conversion.messaging_conversation_started_7d': 'msj_iniciado_7Dias',
    'video_view': 'vistas_video',
    'post_reaction': 'reacciones_post',
    'link_click': 'click_link',
    'post': 'contenido_publicado',
    'onsite_conversion.post_save': 'contenido_guardado',
    'comment': 'comentarios',
    'onsite_conversion.messaging_user_depth_3_message_send': '3er_msj_cliente',
    'like': 'like',
    'onsite_conversion.messaging_welcome_message_view': 'vistas_mensaje_bienvenida',
    'onsite_conversion.messaging_conversation_replied_7d': 'msjs_respondidos_en_7Dias',
    'onsite_conversion.messaging_user_depth_5_message_send': '5to_msj_cliente'
    # Agrega todos los nombres de columnas que deseas cambiar
    
}

# Renombrar las columnas
df.rename(columns=new_column_names, inplace=True)

# Guardar el DataFrame renombrado en un nuevo archivo CSV
df.to_csv("/dbfs/mnt/processed/anuncios_insights_renombrado.csv", index=False)

print("Archivo renombrado y guardado exitosamente.")
display(df)