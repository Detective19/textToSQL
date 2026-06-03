from fastapi import FastAPI
from app.routes.retrieve import router
from app.routes.generate_sql import (
router as sql_router
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Text to SQL API Running"
    }


app.include_router(router)
app.include_router(sql_router)