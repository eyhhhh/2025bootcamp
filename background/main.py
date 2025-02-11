from fastapi import FastAPI
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

