Document clustering:

Document Classifier is a GPU-accelerated semantic document classification pipeline that uses transformer embeddings to sort documents into user-defined categories. It works by extracting and preprocessing text from TXT, PDF, and DOCX files, generating embeddings on the GPU using the BAAI/bge-large-en-v1.5 transformer model (approximately 1.34 GB), and then creating embeddings for each category. Cosine similarity is computed between document and category embeddings to select the best matching category, with a threshold check determining whether a document gets classified or moved to an unclassified folder. The system then moves files into their respective category folders, saves classification metadata as JSON, and writes logs throughout the process.

The project includes features such as GPU-supported embedding generation, semantic classification, user-defined categories, automatic creation of category and unclassified folders, metadata JSON generation, logging support, and batch embedding generation. Its structure consists of core scripts (main.py, pipeline.py, and config.py), and supporting modules (preprocessing.py, embedding.py, similarity.py, file_manager.py, logger.py, and metadata_manager.py).

In terms of requirements, the project is tested on an NVIDIA RTX A5000 GPU and recommends a CUDA-capable NVIDIA GPU with 16 GB or more of VRAM, along with Python 3.10 or higher. The required Python libraries include torch, torchvision, torchaudio, sentence-transformers, transformers, scikit-learn, numpy, pypdf, and python-docx, all installable via pip.

Notes:

The framework requires users to create a directory named "documents" where input files are placed for processing. The framework itself automatically creates a directory named "category", and within this directory, subdirectories are generated dynamically based on the class names specified by the user, such as "civil", "mechanical", and "computer_science" with these categories being fully customizable and varying according to user input in the main execution block.

Configuration of the pipeline is handled through a Config class, which defines several fixed and adjustable parameters. The embedding model is set to "BAAI/bge-large-en-v1.5" via MODEL_NAME, while the DEVICE parameter automatically detects and selects "cuda" if a CUDA-enabled GPU is available, falling back to "cpu" otherwise. The BATCH_SIZE parameter, which controls how many documents are processed together during embedding generation, can be varied by the user as needed. The SIMILARITY_THRESHOLD, set as a fixed default but adjustable, determines the minimum cosine similarity score required for a document to be assigned to a category, with documents falling below this threshold being routed to the unclassified folder. Finally, SUPPORTED_EXTENSIONS defines the list of file formats the pipeline can process, including ".txt" and ".pdf" among others, and this list can also be modified to support additional file types as required.







