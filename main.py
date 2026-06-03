from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from controllers.admin_route import router
from scalar_fastapi import get_scalar_api_reference
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(docs_url=None, redoc_url=None)
# app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():

    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API ",
    )


