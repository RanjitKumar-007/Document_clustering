# Document Classifier

GPU-accelerated semantic document classification pipeline using transformer embeddings.

This project classifies documents into user-defined categories using:

- Semantic embeddings
- Cosine similarity
- GPU acceleration (CUDA)
- Transformer-based language models

Supported document formats:

- TXT
- PDF
- DOCX

---

# Project Workflow

```
Documents
    ↓
Text Extraction
    ↓
Preprocessing
    ↓
GPU Embedding Generation
    ↓
Category Embedding Creation
    ↓
Cosine Similarity
    ↓
Best Category Selection
    ↓
Threshold Checking
    ↓
Move File to Category Folder
    ↓
Save Metadata
    ↓
Write Logs
```

---

# Features

- GPU-supported embedding generation
- Semantic document classification
- User-defined categories
- Automatic category folder creation
- Automatic unclassified folder creation
- Metadata JSON generation
- Logging support
- PDF/DOCX/TXT support
- Batch embedding generation

---

# Project Structure

```
document_classifier/
│
├── main.py
├── pipeline.py
├── config.py
│
├── preprocessing.py
├── embedding.py
├── similarity.py
├── file_manager.py
├── logger.py
├── metadata_manager.py
│
├── models/
│   └── bge-large/
│
├── documents/
│   ├── doc1.txt
│   ├── doc2.pdf
│   └── doc3.docx
│
├── categories/
│   ├── artificial_intelligence/
│   ├── management/
│   ├── civil/
│   ├── Remote_sensing/
│   └── unclassified/
│
├── metadata/
│   └── classification_results.json
│
└── logs/
    └── run.log
```

---

# Requirements

## Hardware

Recommended GPU:

- NVIDIA GPU with CUDA support

Tested GPU:

- NVIDIA RTX A5000

Recommended VRAM:

- 16 GB or higher

---

# Python Environment

Recommended Python version:

```
Python >=3.10
```

---

# Required Libraries

Install required packages:

```
pip install torch torchvision torchaudio
pip install sentence-transformers
pip install transformers
pip install scikit-learn
pip install numpy
pip install pypdf
pip install python-docx
```

---

# Embedding Model

Model used:

- BAAI/bge-large-en-v1.5

Approximate size:

```
~1.34 GB
```