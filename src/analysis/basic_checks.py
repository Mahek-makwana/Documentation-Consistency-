from pathlib import Path
from ingest.docs_loader import load_documents

def check_empty_documents(folder_path=None):
    """
    Check which PDFs/TXT/MD files are empty.
    Returns a list of filenames with zero text.
    """
    docs = load_documents(folder_path)
    empty_files = [doc["name"] for doc in docs if len(doc["content"].strip()) == 0]
    return empty_files

def check_document_lengths(folder_path=None, min_length=50):
    """
    Returns documents that are shorter than min_length characters.
    """
    docs = load_documents(folder_path)
    short_files = [doc["name"] for doc in docs if len(doc["content"].strip()) < min_length]
    return short_files

if __name__ == "__main__":
    folder = Path(__file__).parent.parent.parent / "data" / "docs"
    empty = check_empty_documents(folder)
    short = check_document_lengths(folder)
    print(f"Empty documents: {empty}")
    print(f"Short documents: {short}")



