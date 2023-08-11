from fastapi import FastAPI
import os

os.environ["PYTHON_VERSION"] = "3.10.5"


# Crea una instancia de FastAPI
app = FastAPI()

#1
@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma: str):
    
    return {'idioma':idioma, 'cantidad':int(10)}

#2    
@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion( pelicula: str ):
    return {'pelicula':pelicula, 'duracion':int(15), 'anio':int(2020)}

