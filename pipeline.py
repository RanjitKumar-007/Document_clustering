from preprocessing import load_documents
from embedding import generate_embeddings
from similarity import classify_documents
from file_manager import (
    create_category_directories,
    move_documents
)
from metadata_manager import (
    save_metadata
)
from logger import setup_logger
from config import Config
"""
Main pipeline orchestration module.
Responsibilities:
- Load documents
- Generate GPU embeddings
- Create category embeddings
- Perform semantic classification
- Move documents into category folders
- Save metadata
- Write execution logs
"""
def run_pipeline(input_dir, class_names):
    """
    Execute complete document
    classification pipeline.
    Workflow:
    1. Load documents
    2. Generate embeddings
    3. Generate category embeddings
    4. Compute cosine similarity
    5. Predict best category
    6. Move documents
    7. Save metadata
    8. Write logs
    Args:
        input_dir (str):
            Directory containing input documents
        class_names (list):
            User-defined category names
    """
    logger = setup_logger()
    logger.info(
        "Pipeline started"
    )
    create_category_directories(
        class_names
    )
    documents, filenames = load_documents(
        input_dir
    )
    logger.info(
        f"Loaded {len(documents)} documents"
    )
    if len(documents) == 0:
        print("No documents found.")
        return
    print("\nGenerating embeddings...")
    document_embeddings = generate_embeddings(
        documents
    )
    category_embeddings = generate_embeddings(
        class_names
    )
    logger.info(
        "Embeddings generated successfully"
    )
    predictions = classify_documents(
        document_embeddings,
        category_embeddings,
        class_names
    )
    logger.info(
        "Classification completed"
    )
    move_documents(
        filenames,
        predictions,
        input_dir
    )
    logger.info(
        "Documents moved successfully"
    )
    save_metadata(
        filenames,
        predictions
    )
    logger.info(
        "Metadata saved successfully"
    )
    print("\nClassification Results:\n")
    for file, (category, score) in zip(
        filenames,
        predictions
    ):
        print(
            f"{file}"
            f" --> "
            f"{category}"
            f" ({score:.4f})"
        )
    print("\nPipeline completed.")
    