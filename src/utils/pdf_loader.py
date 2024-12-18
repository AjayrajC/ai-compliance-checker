import time
from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    """Load the PDF and extract content."""
    start_time = time.time()
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    print(f"PDF loaded in {time.time() - start_time:.2f} seconds")
    return docs
