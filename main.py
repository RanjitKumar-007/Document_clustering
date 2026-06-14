import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
from pipeline import run_pipeline
"""
Main entry point for manual user-directed
document classification pipeline.
Workflow:
1. Read input documents
2. Generate GPU embeddings
3. Compare against category embeddings
4. Classify documents
5. Move documents into category folders
"""
if __name__ == "__main__":
    input_dir = "documents" #input folder
    class_names = [ 
        "sentiment_analysis",  #Classes (can vary based user input)
        "coherence_change_detection",
        "image_fusion"
    ]
    run_pipeline(
        input_dir,
        class_names
    )

