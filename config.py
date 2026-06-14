import torch
"""
Global configuration settings for the
document classification pipeline.

Contains:
- Model configuration
- GPU/CPU device selection
- Batch processing settings
- Similarity threshold
- Supported file extensions
- Output directories
- Metadata and logging paths
"""
class Config:
    MODEL_NAME = "BAAI/bge-large-en-v1.5" #Selected embedding model
    DEVICE = (
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )
    BATCH_SIZE = 2 #Batch size can be varied
    SIMILARITY_THRESHOLD = 0.5 #Threshold can be varied
    SUPPORTED_EXTENSIONS = [ #Supported files can be varied
        ".txt",
        ".pdf",
        ".docx"
    ]
    CATEGORY_DIR = "categories"
    LOG_FILE = "logs/run.log"
    METADATA_FILE = (
        "metadata/classification_results.json"
    )
    