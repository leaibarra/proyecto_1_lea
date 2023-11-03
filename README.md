# PROYECTO INDIVIDUAL1


## DATA SCIENCE PT-04
### Leandro Ibarra

Hola! Este es mi primer proyecto individual en la carrera *Data Science* en Henry.
Espero que lo disfruten!!!😁

## INDICE DE ARCHIVOS:
* **Dataframes**: Esta carpeta contiene los datos originales que nos brindo la empresa.
* **Funciones**: En esta carpeta se encuentran los *Data Frames* de las funciones que brindamos.
* **main.py**: En este archivo se encuentra el contenido que se utiliza para *renderizar*.
* **requirments.txt**: En este archivo estan las *librerias* utilizadas en el main.py.
* ****





Para este proyecto nos solicitaron situarnos en un rol de *MLOps Engineer*.


   ![image](https://github.com/leaibarra/proyecto_1_lea/assets/126922100/0064fa02-85cc-4337-9668-7c1984eba1f3)






Hipoteticamente arrancamos a trabajar como Data Scientist en *Steam*, una plataforma multinacional de videojuegos. Y nos solicitan crear un sistema de recomendación de juegos. 

La empresa nos proporciono datos que su maduración es nula😑. En ella nos encontramos con: Datos anidados, de tipo raw, no hay procesos automatizados para la actualización de nuevos productos, entre otras cosas…
Debemos empezar desde 0, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para el cierre del proyecto!


API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permite a diferentes aplicaciones o sistemas interactuar entre sí, permitiendo la comunicación y el intercambio de datos y funcionalidad de manera estandarizada. Se utiliza para integrar servicios, compartir información y automatizar procesos

Nosotros proponemos disponibilizar los datos de la empresa usando FastAPI. FastAPI es un framework web de Python que permite construir APIs de manera rápida, eficiente y fácil de usar. La ide es que pueda ser consumida desde cualquier dispositivo conectado a internet.
Nosotros para mostrar este proyecto utilizaremos RENDER para consumir la API desde la web
Las consultas que proponemos son las siguientes:

> * def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.

> * def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

> * def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

> * def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

> * def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.



Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de hacer el sistema de recomendacion de juegos.

Ofrecemos una propuesta de relación item-item, esto seria que se toma un item y se ve que items son similares al item de entrada.

Nuestro jefe nos pide que el modelo derive obligatoriamente en un GET/POST en la API símil al siguiente formato:

> * def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.


## PRIMER PASO:

 Para comenzar arrancamos con un proceso de carga de la data y procedemos a realizar un proceso de EDA y ETL. Ahi podremos observar con los datos que contamos y realizar las tranformaciones necesarias para cumplir con los objetivos deseados de la empresa.
 Despues de lograr la transformacion procedemos a hacer las funciones que propusimos.
 Este proceso lo podran encontrar en el archivo *"proyecto_1"*


## SEGUNDO PASO:

Una vez realizadas las funciones las cargamos en el archivo *"main.py"* y cargamos las librerias utilizadas en el archivo *"requirments.txt"*. Estos archivos son requisitos indispensables para poder rendedrizar correctamente.

## TERCER PASO:

Luego llegamos al tan ansiado sistema de recomendacion. En el archivo *"EDA_recomendacion"* podran encontrarse con la carga de la data con los datos que nos sirven para llevarlo a cabo. hacemos una limpieza mucho mas profunda y hacemos la función que nos solicito la empresa.
