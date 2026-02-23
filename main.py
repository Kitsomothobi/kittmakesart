# Fastapi core functionality
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Exception handling
from fastapi import HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
# startlette is the actaul framework that handles our acceptions, hence why we need to make an explicit reference to it

# Templates are where we are going to write our html data in oder to make things cleaner and easier to process

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Telling our program where to find templates, aka, our html files
templates = Jinja2Templates(directory="templates")
# From here on out, all our methods will require the request object as an input parameter


# Importing the local data from out makeshift database
from local_db import BLOG_POSTS, fruits

# Our routes currently return json data, in order to turn it into HTML, we need to import HTMLResponse

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    # This says, look in the templates object, and return for us, the home.html file. as a response
        # Additionally, templateRespose takes in an optional 3rd parameter, called the context parameter, this is usally where
        # We will be inserting our json data, in order to have it accessible to the aforementioned html page
    return templates.TemplateResponse(request, "home.html", {"fruits": fruits, "title": "Home"})

@app.get("/blog")
def blog(request: Request):
     return templates.TemplateResponse(request, "blog.html", {"posts": BLOG_POSTS, "title": "Home"})


@app.get("/blog/{post_id}",  include_in_schema=False)
def get_page(request: Request, post_id: int):
    for blog in BLOG_POSTS:
        if blog["id"] == post_id:
            title = blog["title"]
            return templates.TemplateResponse(request, "blog_post.html", {"post": blog, "title": title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found :(")

@app.get("/api/blog")
def blog(request: Request):
    return BLOG_POSTS


# Starlette exception handling
@app.exception_handler(StarletteHTTPException)
def general_htttp_exception_handler(request: Request, exception: StarletteHTTPException):
    # the message object will have detailed information on the type of error, and an occompanying message
    message = (
        exception.detail
        if exception.detail
        else "An error occured, please check your request, and try again"
               )
    # ensuring that an api request must still return json data
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content= {"detail": message}
        )

    #Feeding the error message data, into our error.html file 
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message
        },
        # This ensures the browser doesn't return a 200 response code, in the event of an error occuring
        status_code=exception.status_code 
    )

# RequestValidation Habdling
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, excption: RequestValidationError):
     if request.url.path.startswith("/api"):
         return JSONResponse(
             status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
             content = {"detail": exception.errors()},
         )
     
     return templates.TemplateResponse(
         request,
         "error.html",
         {
             "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
             "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
             "message": "Invalid Request, Please check your input"
         },
         status_code=status.HTTP_422_UNPROCESSABLE_CONTENT
     )