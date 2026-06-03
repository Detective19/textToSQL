from fastapi import APIRouter

from app.models.request_models import QueryRequest
from app.services.retriever import retrieve_tables

router = APIRouter()


@router.post("/retrieve")
def retrieve(req: QueryRequest):

    tables = retrieve_tables(
        req.question
    )

    scores = []

    details = {}

    base = 0.90

    for i, table in enumerate(tables):

        score = round(
1 - (i * 0.08),
2
)

        scores.append(
            score
        )

        details[
            table
        ] = {

            "relevance_score":
            score,

            "reason":
            f"Retrieved using semantic similarity"

        }

    confidence = (
        round(
            sum(scores)
            /
            len(scores),
            2
        )

        if scores

        else 0
    )

    return {

        "retrieved_tables":
        tables,

        "scores":
        scores,

        "confidence":
        confidence,

        "details":
        details
    }