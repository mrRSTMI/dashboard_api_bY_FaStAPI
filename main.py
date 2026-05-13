from fastapi import FastAPI


app = FastAPI(title="tamplate backend")

@app.get("/")
async def mainRoute():
    return {"message":"from mainRoute : Hello frontend and browser ! ! ! "}