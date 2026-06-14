import numpy as np
from sklearn.metrics.pairwise import (
    cosine_similarity
)
from config import Config
"""
Semantic similarity and document
classification module.
Responsibilities:
- Compute cosine similarity
- Compare document embeddings with
  category embeddings
- Select best matching category
- Apply similarity threshold
- Assign unclassified category if needed
"""
def classify_documents(
    document_embeddings,
    category_embeddings,
    class_names
):
    """
    Classify documents based on
    cosine similarity scores.
    Workflow:
    1. Compare document embeddings
       against category embeddings
    2. Select highest similarity score
    3. Apply threshold checking
    4. Assign category
    Args:
        document_embeddings:
            Embeddings generated from
            input documents
        category_embeddings:
            Embeddings generated from
            category names
        class_names (list):
            User-defined category names
    Returns:
        list:
            Predicted category and
            similarity score
    """
    predictions = []
    similarity_matrix = cosine_similarity(
        document_embeddings,
        category_embeddings
    )
    for scores in similarity_matrix:
        best_index = np.argmax(scores)
        best_score = scores[best_index]
        if (
            best_score >=
            Config.SIMILARITY_THRESHOLD
        ):
            category = class_names[best_index]
        else:
            category = "unclassified"
        predictions.append(
            (
                category,
                float(best_score)
            )
        )
    return predictions
