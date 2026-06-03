from fastapi import APIRouter

from app.models.request_models import QueryRequest
from app.services.retriever import retrieve_tables
from app.services.sql_generator import generate_sql


router = APIRouter()


@router.post("/generate-sql")
def generate(req: QueryRequest):

    tables = retrieve_tables(
        req.question
    )

    sql = generate_sql(
        req.question,
        tables
    )

    return {

        "question":
        req.question,

        "retrieved_tables":
        tables,

        "sql":
        sql

    }