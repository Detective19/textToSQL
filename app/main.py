from fastapi import FastAPI
from app.routes.retrieve import router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Text to SQL API Running"
    }


app.include_router(router)