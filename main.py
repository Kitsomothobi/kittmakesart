from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Templates are where we are going to write our html data in oder to make things cleaner and easier to process

app = FastAPI()

fruits = [
    {
    "id": 1 ,
    "type": "Citrus",
    "name": "Orange"
    },
    {
    "id": 2 ,
    "type": "Citrus",
    "name": "Lemon"
    },

    {
    "id": 3 ,
    "type": "Exotic",
    "name": "Dragon Fruit"
    }
    
    ]

# Our routes currently return json data, in order to turn it into HTML, we need to import HTMLResponse
@app.get("/")
def greetings():
    return fruits


@app.get("/fruit")
def fruit():
    return fruits