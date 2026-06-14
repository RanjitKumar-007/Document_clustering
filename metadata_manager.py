import json
import os
from config import Config
"""
Metadata management module.
Responsibilities:
- Store classification results
- Save predicted categories
- Save similarity scores
- Generate JSON metadata output
"""
def save_metadata(filenames, predictions):
    """
    Save document classification
    results into JSON file.
    Args:
        filenames (list):
            List of document filenames
        predictions (list):
            Predicted category and
            similarity score
    """
    os.makedirs(
        "metadata",
        exist_ok=True
    )
    results = []
    for file, (category, score) in zip(
        filenames,
        predictions
    ):
        results.append(
            {
                "document": file,
                "category": category,
                "similarity_score": score
            }
        )
    with open(
        Config.METADATA_FILE,
        "w"
    ) as f:
        json.dump(
            results,
            f,
            indent=4
        )
        