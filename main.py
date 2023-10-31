from fastapi import FastAPI
import pandas as pd

#Instanciamos la aplicacion
app = FastAPI()

funcion_1_completo = pd.read_parquet("Funciones/funcion_1.parquet")
funcion_2_completo = pd.read_parquet("Funciones/funcion_2.parquet")
funcion_3_completo = pd.read_parquet("Funciones/funcion_3.parquet")
funcion_4_completo = pd.read_parquet("Funciones/funcion_4.parquet")
funcion_5_completo = pd.read_parquet("Funciones/funcion_5.parquet")

# Obtener una muestra del 10% de los datos
funcion_1 = funcion_1_completo.sample(frac=0.10, random_state=1)
funcion_2 = funcion_2_completo.sample(frac=0.10, random_state=1)
funcion_3 = funcion_3_completo.sample(frac=0.10, random_state=1)
funcion_4 = funcion_4_completo.sample(frac=0.10, random_state=1)
funcion_5 = funcion_5_completo.sample(frac=0.10, random_state=1)



@app.get("/PlayTimeGenre/{genero}", name= "Tiempo de juego por genero")
async def PlayTimeGenre(genero: str):
    # Filtrar el DataFrame para obtener solo las filas del género específico
    funcion_1_filtrado = funcion_1[funcion_1['genres'].str.contains(genero, case=False, na=False)]

    if funcion_1_filtrado.empty:
        return "No se encontraron datos para el género especificado."

    # Encontrar el año con más horas jugadas
    año_con_mas_horas = funcion_1_filtrado.groupby('release_date')['playtime_forever'].sum().idxmax()

    return {"Año de lanzamiento con más horas jugadas para Género " + genero: año_con_mas_horas}




