from langchain.chains import RetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key="")

def retrieval(query):
    vector_store = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4-turbo", openai_api_key=""),
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )

    # query = "how do i get a free insurance policy?"
    # instruction = "If it is not present in the document, just mention 'I don't have information regarding this, you may contact www.uiic.co.in'"
    response = qa_chain.invoke(query+". instruction: Give the response in a single paragraph and with a combination of telugu and english and maintain it throught the response. Example: Next week travel plans ఉన్నాయా? నేను Hyderabad వెళ్లాలి because office work ఉంది. Flight tickets book చేయాలని thinking, but timings confirm కాలేదు. If you are free, let's plan together.")

    print("Answer:", response["result"])
    return str(response["result"])

    # print("Sources:", [doc.metadata for doc in response["source_documents"]])

# retrieval()
