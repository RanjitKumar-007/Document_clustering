from sentence_transformers import SentenceTransformer
from config import Config
"""
Embedding generation module.
Responsibilities:
- Load embedding model
- Use GPU acceleration if available
- Generate normalized semantic embeddings
- Support batch processing for efficiency
"""
model = SentenceTransformer(
    Config.MODEL_NAME,
    device=Config.DEVICE
)
def generate_embeddings(texts):
    """
    Generate semantic embeddings for input texts.
    Args:
        texts (list):
            List of preprocessed document texts
    Returns:
        numpy.ndarray:
            Normalized embedding vectors
    """
    embeddings = model.encode(
        texts,
        batch_size=Config.BATCH_SIZE,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True
    )
    return embeddings
