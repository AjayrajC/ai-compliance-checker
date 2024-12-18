from src.utils.pdf_loader import load_pdf
from src.utils.text_chunker import split_text
from src.utils.embeddings import create_embeddings
from src.controllers.context_retriever import retrieve_context 
from src.controllers.report_generator import generate_report
from src.config.config import VECTOR_INDEX, CHUNK_SIZE, CHUNK_OVERLAP

def main():
    pdf_path = "data/data-modernization-the-foundation-for-digital-transformation-codex5343.pdf"

    # 1. PDF Loading and Text Extraction
    print("Loading PDF...")
    docs = load_pdf(pdf_path)

    # 2. Chunking Text
    print("Splitting text into chunks...")
    chunks = split_text(docs, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    # 3. Embedding Generation and Vector Storage
    print("Generating embeddings and storing in Pinecone...")
    create_embeddings(chunks, VECTOR_INDEX)

    # 4. Context Retrieval
    print("Retrieving context...")
    context = retrieve_context()

    # 5. Report Generation
    print("Generating compliance report...")
    report_path = generate_report(context)

    print(f"Report successfully saved at: {report_path}")

if __name__ == "__main__":
    main()
