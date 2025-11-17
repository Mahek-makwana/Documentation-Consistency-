import fitz  # PyMuPDF 
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "docs"

def load_documents(folder_path=None):
    """
    Load all PDF, TXT, and MD files from the default DATA_PATH or a custom folder.
    Returns a list of dictionaries: [{"name": filename, "content": text}, ...]
    """
    documents = []
    folder = Path(folder_path) if folder_path else DATA_PATH

    for file in folder.glob("*"):
        if file.suffix.lower() == ".pdf":
            doc = fitz.open(file)
            text = ""
            for page in doc:
                text += page.get_text()
            documents.append({"name": file.name, "content": text})

        elif file.suffix.lower() in [".txt", ".md"]:
            text = file.read_text(encoding="utf-8", errors="ignore")
            documents.append({"name": file.name, "content": text})

    return documents


