from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name: str
    score: int

@app.get("/test")
def test():
    return {"message": "API working"}

@app.post("/submit")
def submit(data: Data):
    return {
        "status": "received",
        "name": data.name,
        "score": data.score
    }
