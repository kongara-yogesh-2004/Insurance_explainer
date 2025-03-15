from langchain_community.document_loaders import PyMuPDFLoader  # For extracting text from PDFs
from langchain.text_splitter import RecursiveCharacterTextSplitter
import neuraoak_embedding
import query_retrieval

# Load the policy PDF
pdf_path = "./health_insurance_policy.pdf"
loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

# Split text into manageable chunks for embedding
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

print(f"Extracted {len(chunks)} chunks from PDF")
embedding_status = neuraoak_embedding.create_embedding(chunks= chunks)
if(embedding_status):
    print("Embeddings created successfully")