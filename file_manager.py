import os
import shutil
from config import Config
"""
File and directory management module.
Responsibilities:
- Create category directories
- Create unclassified directory
- Move classified documents
- Preserve original file metadata
"""
def create_category_directories(class_names):
    """
    Create category folders based on
    user-defined class names.
    Also creates:
    - categories/
    - unclassified/
    """
    os.makedirs(
        Config.CATEGORY_DIR,
        exist_ok=True
    )
    for name in class_names:
        path = os.path.join(
            Config.CATEGORY_DIR,
            name
        )
        os.makedirs(
            path,
            exist_ok=True
        )
    os.makedirs(
        os.path.join(
            Config.CATEGORY_DIR,
            "unclassified"
        ),
        exist_ok=True
    )
def move_documents(filenames, predictions, input_dir):
    """
    Move documents into predicted
    category folders.
    Args:
        filenames (list):
            List of document filenames
        predictions (list):
            Predicted category and
            similarity score
        input_dir (str):
            Source document directory
    """
    for file, (category, _) in zip(
        filenames,
        predictions
    ):
        source = os.path.join(
            input_dir,
            file
        )
        destination = os.path.join(
            Config.CATEGORY_DIR,
            category,
            file
        )
        shutil.copy2(
            source,
            destination
        )
        