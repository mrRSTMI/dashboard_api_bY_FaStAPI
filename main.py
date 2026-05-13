from fastapi import FastAPI
from controllers.admin_route import router

app = FastAPI(title="tamplate backend")
app.include_router(router=router)
@app.get("/")
async def mainRoute():
    return {"message":"from mainRoute : Hello frontend and browser ! ! ! "}