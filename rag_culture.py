from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def rag_query(query):
    with open("data/culture_knowledge/global_culture.txt", "r", encoding="utf-8") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    store = FAISS.from_texts(chunks, embed)

    llm = Ollama(model="phi3")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=store.as_retriever())
    return qa.run(query)
