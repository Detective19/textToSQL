from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from app.data.load_schema import get_schema


SCHEMA = get_schema()


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


schema_vectors = model.encode(
    SCHEMA,
    normalize_embeddings=True
)


index = faiss.IndexFlatIP(
    schema_vectors.shape[1]
)

index.add(
    np.array(schema_vectors)
)


def retrieve_tables(
    question,
    k=5
):

    query = model.encode(
        [question],
        normalize_embeddings=True
    )

    scores, indices = index.search(
        np.array(query),
        k
    )

    results = []

    for score, idx in zip(
        scores[0],
        indices[0]
    ):

        if score > 0.30:

            table = (
                SCHEMA[idx]
                .split(":")[0]
            )

            results.append(
                table
            )

    if not results:

        return [
            SCHEMA[
                indices[0][0]
            ].split(":")[0]
        ]

    return results