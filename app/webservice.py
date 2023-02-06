# IMPORTATION PYTHON
import requests
import uvicorn

# IMPORTATION FASTAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# définition des autorisations d'accès aux services
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DÉCLARATION DES VARIABLES GLOBALES
app.status = "start"
app.last_dog = ""


# DÉCLARATION DES ENDPOINTS
@app.get("/getDog/")
def getDog():
    if app.status == "start":
        app.last_dog = get_random_dog()
        return app.last_dog
    else:
        return app.last_dog

@app.put("/stop/")
def stop_function():
    """
    this functions change the status from start to stop
    """
    app.status = "stop"
    return {}

@app.put("/start/")
def start_function():
    """
    this functions change the status from stop to start
    """
    app.status = "start"
    return {}


# DÉCLARATION DES FONCTIONS
def get_random_dog() -> dict:
    """
    this function allows to retrieve a random image of a dog
    and extract the breed name from the image link
    """
    reponse = requests.get('https://dog.ceo/api/breeds/image/random')
    data = eval(reponse.content)
    race = data['message'].split('/')[4]
    return {'name': race, "image": data['message']}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)