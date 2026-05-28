from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from controllers.admin_route import router

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router)




@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    html_content = """

    <!DOCTYPE html>
    <html>
    <head>
    <title>Scalar Offline API Reference</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
    <body>
    
    <script id="api-reference" data-url="/openapi.json"></script>
    
    <script src="/static/standalone.js"></script>
    </body>
    </html>
    """
    return HTMLResponse(html_content)
