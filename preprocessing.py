import os
from pypdf import PdfReader
from docx import Document
from config import Config
"""
Document loading and text extraction module.
Responsibilities:
- Read .txt documents
- Read .pdf documents
- Read .docx documents
- Extract textual content
- Filter unsupported files
- Return document texts and filenames
"""
def read_txt(file_path):
    """
    Read text file content.
    Args:
        file_path (str):
            Path to .txt file
    Returns:
        str:
            Extracted text
    """
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()
def read_pdf(file_path):
    """
    Extract text from PDF document.
    Args:
        file_path (str):
            Path to .pdf file
    Returns:
        str:
            Extracted text
    """
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text
def read_docx(file_path):
    """
    Extract text from DOCX document.
    Args:
        file_path (str):
            Path to .docx file
    Returns:
        str:
            Extracted text
    """
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)
def load_documents(input_dir):
    """
    Load and extract text from
    supported documents.
    Supported formats:
    - .txt
    - .pdf
    - .docx
    Args:
        input_dir (str):
            Input document directory
    Returns:
        tuple:
            documents (list)
            filenames (list)
    """
    documents = []
    filenames = []
    for file in os.listdir(input_dir):
        extension = os.path.splitext(file)[1].lower()
        if extension not in Config.SUPPORTED_EXTENSIONS:
            continue
        file_path = os.path.join(
            input_dir,
            file
        )
        try:
            if extension == ".txt":
                text = read_txt(file_path)
            elif extension == ".pdf":
                text = read_pdf(file_path)
            elif extension == ".docx":
                text = read_docx(file_path)
            else:
                continue
            if not text.strip():
                continue
            documents.append(text)
            filenames.append(file)
        except Exception as e:
            print(
                f"Error reading {file}: {e}"
            )
    return documents, filenames
