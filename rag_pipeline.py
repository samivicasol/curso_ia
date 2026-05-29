from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import config
import os

def get_vector_db(documents=None):
    """Inicializa o carga la base de datos vectorial ChromaDB."""
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    
    if documents:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)
        return Chroma.from_documents(
            documents=chunks, 
            embedding=embeddings, 
            persist_directory=config.CHROMA_PATH
        )
    return Chroma(persist_directory=config.CHROMA_PATH, embedding_function=embeddings)

def get_qa_chain():
    """Configura la cadena de QA con Groq."""
    db = get_vector_db()
    retriever = db.as_retriever(search_kwargs={"k": 5})
    llm = ChatGroq(groq_api_key=config.GROQ_API_KEY, model_name=config.LLM_MODEL)
    
    system_prompt = (
        "Eres un asistente para tareas de preguntas y respuestas. "
        "Usa los siguientes fragmentos de contexto recuperado para responder la pregunta. "
        "Si no sabes la respuesta, di que no la sabes."
        "\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("human", "{input}")]
    )
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, combine_docs_chain)