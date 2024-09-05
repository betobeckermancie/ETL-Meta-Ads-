import pandas as pd

df =pd.read_csv("/dbfs/mnt/processed/anuncios_insights_expanded.csv")
#Convertir columnas a tipo numero

columns_to_convert=['onsite_conversion.messaging_user_depth_2_message_send',
       'onsite_conversion.messaging_conversation_started_7d', 'video_view',
       'post_reaction', 'link_click', 'post', 'onsite_conversion.post_save',
       'comment', 'onsite_conversion.messaging_user_depth_3_message_send',
       'like', 'onsite_conversion.messaging_welcome_message_view',
       'onsite_conversion.messaging_conversation_replied_7d',
       'onsite_conversion.messaging_user_depth_5_message_send']
#convertir cada columna a tipo numerico
for column in columns_to_convert:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    else:
        print(f"Column {column} does not exist in DataFrame.")

#guardar el csv modificado
df.to_csv("/dbfs/mnt/processed/anuncios_insights_expanded_numeric.csv", index=False)

#mostrar cambio
display(df)