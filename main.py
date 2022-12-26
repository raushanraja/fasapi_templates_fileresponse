# import fastapi library
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

# create an instance of FastAPI
app = FastAPI()


# mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
# add jinja2 template and related code to return html file
templates = Jinja2Templates(directory="templates")


# create a route
@app.get("/")
def index():
    return {"message": "Hello World"}


# create a route to return html file using jinja2 template
@app.get("/html")
def html(request: Request):
    # return the html file using jinja2 template
    return templates.TemplateResponse("item.html", {"request": request, "id": "1"})

# create a route pdf


@app.get("/pdf")
def pdf():
    # return a pdf file using fileResponse
    from fastapi.responses import FileResponse
    # get path of the pdf file using pathlib from current pdfs folder
    from pathlib import Path
    path = Path(__file__).parent / "pdfs" / "sip.pdf"
    print(path)
    return FileResponse(path=path, media_type="application/pdf")


# run the app
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host='0.0.0.0', reload=True)
