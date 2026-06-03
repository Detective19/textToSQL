from datasets import load_dataset


def get_schema():

    dataset = load_dataset(
        "beaverbench/beaver-table"
    )

    schemas = []

    for split in dataset:

        for row in dataset[split]:

            table = row[
                "table_name"
            ]

            cols = ", ".join(
                row[
                    "column_names"
                ]
            )

            schemas.append(
                f"{table}: {cols}"
            )

    return schemas