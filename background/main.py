from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<html>
    <head><title></title>
    <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="text" name="name" />
            <br />
            
            <input type="file" name="files" />
            <input type="file" name="files" />
            <input type="file" name="files" />
            
            <br /><br />
            <input type="submit" />
        </form>
    </body>
</html>
"""
@app.get('/')
def home():
    return HTMLResponse(html)

@app.post('/upload')
def upload(files: list[UploadFile] | None = None):
    arFiels = []
    for file in arFiels:
        if file.filename < 1:
            continue
        arFiels.append(file.filename)
    return arFiels
