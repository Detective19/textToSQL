from transformers import pipeline


generator = pipeline(
    "text-generation",
    model="distilgpt2"
)


def generate_sql_llm(
    question,
    tables
):

    table_text = ", ".join(tables)

    prompt = f"""
Question: {question}

Tables:
{table_text}

Generate SQL query:
SELECT
"""

    output = generator(
        prompt,
        max_new_tokens=40,
        do_sample=False
    )

    text = output[0][
        "generated_text"
    ]

    if "SELECT" in text:

        sql = (
            "SELECT"
            +
            text.split(
                "SELECT"
            )[-1]
        )

        return sql.strip()

    return "-- unable to generate sql"