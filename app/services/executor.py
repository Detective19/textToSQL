import sqlite3


def execute_sql(sql):

    try:

        conn = sqlite3.connect(
            "app/data/demo.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
SELECT name
FROM sqlite_master
WHERE type='table'
"""
        )

        tables = [
            row[0]
            for row in cursor.fetchall()
        ]

        requested = None

        if "FROM" in sql.upper():

            requested = (
                sql
                .upper()
                .split("FROM")[1]
                .split()[0]
                .strip()
            )

        if (
            requested
            and
            requested.lower()
            not in [
                t.lower()
                for t in tables
            ]
        ):

            conn.close()

            return {
                "execution_skipped":
                True,

                "reason":
                f"table {requested} not available in sqlite demo db"
            }

        cursor.execute(
            sql
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    except Exception as e:

        return str(e)