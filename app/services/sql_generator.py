from app.services.llm_sql import (
    generate_sql_llm
)


def fallback_sql(
    question,
    tables
):

    q = question.lower()

    if "student" in q:

        return f"""
SELECT *
FROM {tables[0]}
LIMIT 10
""".strip()

    return "-- unable to generate sql"


def generate_sql(
    question,
    tables
):

    sql = generate_sql_llm(
        question,
        tables
    )

    if (
        sql is None
        or
        len(sql.strip()) < 15
        or
        sql.strip().upper() == "SELECT"
    ):

        return fallback_sql(
            question,
            tables
        )

    return sql