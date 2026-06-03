import sqlglot


def validate_sql(
    sql
):

    try:

        sqlglot.parse_one(
            sql
        )

        return True

    except Exception:

        return False