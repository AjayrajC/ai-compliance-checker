from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(docs, chunk_size=1000, chunk_overlap=200):
    """Split text into smaller overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)
