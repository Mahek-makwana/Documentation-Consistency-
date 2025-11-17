from tree_sitter import Language, Parser
from ingest.docs_loader import load_documents
from analysis.basic_checks import check_empty_documents, check_document_lengths

# Minimum length threshold for “short” documents
MIN_LENGTH = 50

# Optional: ignore small files like readme.md
IGNORE_FILES = ["readme.md"]

def test_tree_sitter():
    print("Tree-sitter imported successfully!")

def main():
    # Test tree-sitter import
    test_tree_sitter()

    # Load documents
    docs = load_documents()
    print(f"Loaded {len(docs)} documents\n")

    # Run basic analysis
    empty_docs = check_empty_documents()
    short_docs = check_document_lengths(min_length=MIN_LENGTH)

    # Remove ignored files from short_docs
    short_docs = [doc for doc in short_docs if doc not in IGNORE_FILES]

    print("=== Document Analysis Results ===\n")
    for doc in docs:
        name = doc["name"]
        content_length = len(doc["content"].strip())

        if name in empty_docs:
            issue = "Document is empty"
        elif name in short_docs:
            issue = f"Document is too short ({content_length} chars)"
        else:
            issue = "No issues"

        print(f"File: {name}")
        print(f"Length: {content_length} characters")
        print(f"Issue: {issue}\n")

if __name__ == "__main__":
    main()


   




