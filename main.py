from fastapi import FastAPI
import pandas as pd

#Instanciamos la aplicacion
app = FastAPI()

funcion_1 = pd.read_parquet("Funciones/funcion_1.parquet")
funcion_2 = pd.read_parquet("Funciones/funcion_2.parquet")
funcion_3 = pd.read_parquet("Funciones/funcion_3.parquet")
funcion_4 = pd.read_parquet("Funciones/funcion_4.parquet")
funcion_5 = pd.read_parquet("Funciones/funcion_5.parquet")



@app.get("/PlayTimeGenre/{genero}", name= "Tiempo de juego por genero")
async def PlayTimeGenre(genero):
    # Filtramos el DataFrame para obtener solo las filas del género específico
    funcion_1_filtrado = funcion_1[funcion_1['genres'].str.contains(genero, case=False)]

    if funcion_1_filtrado.empty:
        return "No se encontraron datos para el género especificado."

    # Agrupamos por año y sumamos las horas jugadas
    resumen = funcion_1_filtrado.groupby('release_date')['playtime_forever'].sum()

    # Encontramos el año con la suma máxima de horas jugadas
    año_con_mas_horas = resumen.idxmax()

    return {"El año con más horas jugadas para el genero": genero, "es:": año_con_mas_horas}

'''
@app.get("/UserForGenre/{genero}", name= "Usuario con mas horas")
async def UserForGenre(genero):
    # Filtramos los datos por el género proporcionado
    data_f = funcion_2[funcion_2['genres'] == genero]

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
    data_filtrada = funcion_3[funcion_3['posted'] == anio]


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
    data_filtrada = funcion_4[funcion_4['posted'] == anio]

    # Calculamos la suma de recomendaciones para cada juego
    recomendaciones_por_juego = data_filtrada.groupby('app_name')['sentiment_analysis'].sum().reset_index()

    # Clasificamos los juegos en función de la suma de recomendaciones (de menor a mayor)
    juegos_menos_recomendados = recomendaciones_por_juego.sort_values(by='sentiment_analysis').head(3)

    # Creamos la estructura de resultado deseada
    resultado = [{"Puesto " + str(i + 1): juego + " " + str(recomendaciones) + " recomendaciones obtuvo"} for i, juego, recomendaciones in
                zip(range(3), juegos_menos_recomendados['app_name'], juegos_menos_recomendados['sentiment_analysis'])]

    return resultado


@app.get("/sentiment_analysis/{año}", name= "registros de reseñas de usuarios")
async def sentiment_analysis(anio:int):
    positivo = 0
    neutro = 0
    negativo = 0

    # Filtrar los datos para el año especificado
    funcion_5_f = funcion_5[funcion_5['release_date'] == anio]

    for index, row in funcion_5_f.iterrows():
         if row['sentiment_analysis'] == 2:
            positivo += 1
         elif row['sentiment_analysis'] == 1:
            neutro += 1
         else:
            negativo += 1
    return ('Positivos: ', positivo, ' Neutros: ', neutro, ' Negativos: ', negativo)
'''
