# following https://fastapi.tiangolo.com/deployment/docker/
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello local server"}
