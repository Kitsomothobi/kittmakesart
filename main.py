from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Templates are where we are going to write our html data in oder to make things cleaner and easier to process

app = FastAPI()

# Telling our program where to find templates, aka, our html files
templates = Jinja2Templates(directory="templates")
# From here on out, all our methods will require the request object as an input parameter


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
def greetings(request: Request):
    # This says, look in the templates object, and return for us, the home.html file. as a response
        # Additionally, templateRespose takes in an optional 3rd parameter, called the context parameter, this is usally where
        # We will be inserting our json data, in order to have it accessible to the aforementioned html page
    return templates.TemplateResponse(request, "home.html", {"fruits": fruits, "title": "Home"})


@app.get("/fruit")
def fruit():
    return fruits