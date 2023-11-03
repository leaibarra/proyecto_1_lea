from fastapi import FastAPI
import pandas as pd

#Instanciamos la aplicacion
app = FastAPI()

funcion_1_main = pd.read_parquet("Funciones/funcion_1_muestra.parquet")
funcion_2_main = pd.read_parquet("Funciones/funcion_2_muestra.parquet")
funcion_3_main = pd.read_parquet("Funciones/funcion_3_muestra.parquet")
funcion_4_main = pd.read_parquet("Funciones/funcion_4_muestra.parquet")
funcion_5_main = pd.read_parquet("Funciones/funcion_5_muestra.parquet")
sin_usuario = pd.read_parquet("Funciones/sin_usuario.parquet")


@app.get("/PlayTimeGenre/{genero}", name= "Tiempo de juego por genero")
async def PlayTimeGenre(genero: str):
    # Filtrar el DataFrame para obtener solo las filas del género específico
    funcion_1_filtrado = funcion_1_main[funcion_1_main['genres'].str.contains(genero, case=False, na=False)]

    if funcion_1_filtrado.empty:
        return "No se encontraron datos para el género especificado."

    # Encontrar el año con más horas jugadas
    año_con_mas_horas = funcion_1_filtrado.groupby('release_date')['playtime_forever'].sum().idxmax()

    return {"Año de lanzamiento con más horas jugadas para Género " + genero: año_con_mas_horas}


@app.get("/UserForGenre/{genero}", name= "Usuario con mas horas")
async def UserForGenre(genero):
    # Filtramos los datos por el género proporcionado
    data_f = funcion_2_main[funcion_2_main['genres'] == genero]

    # Calculamos las horas jugadas por usuario y año
    grouped_data = data_f.groupby(['user_id'])['playtime_forever'].sum().reset_index()

    # Encontramos al usuario con la máxima acumulación de horas jugadas
    max_user = grouped_data.groupby('user_id')['playtime_forever'].sum().idxmax()

    # Filtramos los datos para el usuario con más horas jugadas
    max_user_data = grouped_data[grouped_data['user_id'] == max_user]

    # Creamos una lista de la acumulación de horas jugadas por año
    horas_por_año = data_f.groupby('posted')['playtime_forever'].sum().reset_index()
    horas_por_año_dict = [{"Año": año, "Horas": horas} for año, horas in zip(horas_por_año['posted'], horas_por_año['playtime_forever'])]


    resultado = {
        "Usuario con más horas jugadas para el género " + genero: max_user,
        "Horas jugadas por año": horas_por_año_dict
    }

    return resultado


@app.get("/UsersRecommend/{año}", name= "top 3 de juegos MÁS recomendados por usuarios para el año dado")
async def UsersRecommend(anio:int):
    # Filtramos los datos para el año especificado
    data_filtrada = funcion_3_main[funcion_3_main['posted'] == anio]


    # Calculamos la cantidad de recomendaciones para cada juego
    recomendacion = data_filtrada['app_name'].value_counts().reset_index()
    recomendacion.columns = ['app_name', 'recommend']

    # Clasificamos los juegos en función de la cantidad de recomendaciones
    top_3_games = recomendacion.sort_values(by='recommend', ascending=False).head(3)

    # Creamos la estructura de resultado deseada
    resultado = []

    for i, juego, recomendaciones in zip(range(1, 4), top_3_games['app_name'], top_3_games['recommend']):
        resultado.append(f"Puesto {i}: {juego} {recomendaciones}")

    return resultado


@app.get("/UsersNotRecommend/{año}", name= "top 3 de juegos MENOS recomendados por usuarios para el año dado")
async def UsersNotRecommend(anio:int):
    # Filtramos los datos para el año especificado
    data_filtrada = funcion_4_main[funcion_4_main['posted'] == anio]

    # Calculamos la suma de recomendaciones para cada juego
    recomendaciones_por_juego = data_filtrada.groupby('app_name')['sentiment_analysis'].sum().reset_index()

    # Clasificamos los juegos en función de la suma de recomendaciones (de menor a mayor)
    juegos_menos_recomendados = recomendaciones_por_juego.sort_values(by='sentiment_analysis').head(3)

    # Creamos la estructura de resultado deseada
    resultado = [{"Puesto " + str(i + 1): juego + " " + str(recomendaciones) + " recomendaciones obtuvo"} for i, juego, recomendaciones in
                zip(range(3), juegos_menos_recomendados['app_name'], juegos_menos_recomendados['sentiment_analysis'])]

    return resultado


@app.get("/sentiment_analysis/{año}", name= "registros de reseñas de usuarios")
async def sentiment_analysis(anio: int):
    # Filtrar los datos para el año especificado y contar las categorías de sentimiento
    funcion_5_f = funcion_5_main[funcion_5_main['release_date'] == anio]
    sentiment_counts = funcion_5_f['sentiment_analysis'].value_counts().to_dict()

    # Crear un diccionario con los resultados
    results = {
        'Negative': sentiment_counts.get(0, 0),
        'Neutral': sentiment_counts.get(1, 0),
        'Positive': sentiment_counts.get(2, 0)
    }

    return results


@app.get("/recomendacion_juego/{id}", name= "sistema de recomendacion")
async def recomendacion_juego(id_ingresado):
    # Verificar si el 'id_ingresado' está en la columna 'id'
    if id_ingresado in sin_usuario['id'].values:
        # Filtrar por 'id'
        df_filtrado = sin_usuario[sin_usuario['id'] == id_ingresado]

        # Filtrar por 'genres'
        if not df_filtrado.empty:
            genre = df_filtrado.iloc[0]['genres']
            df_filtrado = sin_usuario[sin_usuario['genres'] == genre]

            # Filtrar por 'specs'
            if not df_filtrado.empty:
                df_filtrado = df_filtrado[df_filtrado['specs'] == df_filtrado.iloc[0]['specs']]

                # Filtrar por 'developer'
                if not df_filtrado.empty:
                    df_filtrado = df_filtrado[df_filtrado['developer'] == df_filtrado.iloc[0]['developer']]

                    # Filtrar por 'funny_number'
                    if not df_filtrado.empty:
                        df_filtrado = df_filtrado.sort_values(by='funny_number', ascending=False)

                        # Devolver los nombres de los juegos recomendados
                        if not df_filtrado.empty:
                            nombres_recomendados = df_filtrado['app_name'].iloc[:5].tolist()
                            return nombres_recomendados
            else:
                return "No se encontraron juegos con los mismos criterios."
        else:
            return "No se encontraron juegos con el género ingresado."
    else:
        return "No se encontraron juegos con el ID ingresado."






