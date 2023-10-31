from fastapi import FastAPI
import pandas as pd

#Instanciamos la aplicacion
app = FastAPI()

funcion_1_completo = pd.read_parquet("Funciones/funcion_1.parquet")
funcion_2_completo = pd.read_parquet("Funciones/funcion_2.parquet")
funcion_3_completo = pd.read_parquet("Funciones/funcion_3.parquet")
funcion_4_completo = pd.read_parquet("Funciones/funcion_4.parquet")
funcion_5_completo = pd.read_parquet("Funciones/funcion_5.parquet")




