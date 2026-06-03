from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from app.data.schema import SCHEMA


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Create embeddings
schema_vectors = model.encode(
    SCHEMA,
    normalize_embeddings=True
)

# Build index
dimension = schema_vectors.shape[1]

index = faiss.IndexFlatIP(
    dimension
)

index.add(
    np.array(schema_vectors)
)


def retrieve_tables(
    question,
    k=5,
    threshold=0.65
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

        if score >= threshold:

            results.append(
                {
                    "table": SCHEMA[idx].split(":")[0],
                    "score": float(score)
                }
            )

    if not results:
        return ["unknown"]

    return [
        x["table"]
        for x in results
    ]