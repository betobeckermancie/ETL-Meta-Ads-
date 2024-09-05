#expandir a detalle columna actions y guardarla
import pandas as pd
import json

#cargar el csv guardado
df = pd.read_csv("/dbfs/mnt/processed/anuncios_insightsTEST.csv")

#Funcion para expandir columna actions
def expand_actions(actions):
    try:
        actions_list = json.loads(actions.replace("'", "\""))
        expanded = {action['action_type']: action['value'] for action in actions_list}
        return pd.Series(expanded)
    except Exception as e:
        print(f"Error al procesar la fila: {e}")
        return pd.Series()
    
#se aplica la funcion a la columna 'actions' y concatena los resultados
df_expanded = df['actions'].apply(expand_actions)

#concatenar las columnas nuevas con el Dataframe original
df_final = pd.concat([df.drop('actions', axis=1), df_expanded], axis=1)

#guardar el resultado en el CSV
df_final.to_csv("/dbfs/mnt/processed/anuncios_insights_expanded.csv", index=False)
print(df_final.columns)

#Revisar cambios
display(df_final)
print(df.columns)