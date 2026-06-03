from fastapi import APIRouter
from app.models.request_models import QueryRequest
from app.services.retriever import retrieve_tables

router = APIRouter()


@router.post("/retrieve")
def retrieve(
    req: QueryRequest
):

    tables = retrieve_tables(
        req.question
    )

    return {
        "question": req.question,
        "retrieved_tables": tables
    }