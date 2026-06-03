from fastapi import APIRouter

from app.models.request_models import QueryRequest
from app.services.retriever import retrieve_tables
from app.services.sql_generator import generate_sql
from app.services.validator import validate_sql
from app.services.executor import execute_sql

router = APIRouter()


@router.post(
"/generate-sql"
)
def generate(
req: QueryRequest
):

    tables = []

    if req.use_retrieved_context:

        tables = retrieve_tables(
            req.question
        )

    sql = generate_sql(
        req.question,
        tables
    )

    valid = validate_sql(
        sql
    )

    result = None

    if valid:

        result = execute_sql(
            sql
        )

    return {

        "question":
        req.question,

        "use_retrieved_context":
        req.use_retrieved_context,

        "retrieved_tables":
        tables,

        "sql":
        sql,

        "valid":
        valid,

        "result":
        result
    }