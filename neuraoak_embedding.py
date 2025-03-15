from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_embedding(chunks: list):
    embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="")

    vector_store = FAISS.from_documents(chunks, embedding_model)
    vector_store.save_local("faiss_index")
    return True
