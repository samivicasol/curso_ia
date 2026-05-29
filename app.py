import streamlit as st
import os
import config
from document_loader import load_documents
from rag_pipeline import get_vector_db, get_qa_chain

st.set_page_config(page_title="RAG Agent - Groq", layout="wide")
st.title("🤖 RAG Agent con Streamlit y Groq")

# Sidebar para gestión de documentos
with st.sidebar:
    st.header("Gestión de Documentos")
    st.write(f"Directorio: `{config.DATA_DIR}/`")
    
    if st.button("Reindexar Documentos"):
        with st.spinner("Procesando documentos..."):
            docs = load_documents(config.DATA_DIR)
            if docs:
                st.session_state.vector_db = get_vector_db(docs) # Guardar la DB en el estado de sesión
                st.success(f"¡{len(docs)} documentos indexados!")
            else:
                st.error("No se encontraron documentos compatibles.")

    if st.button("Limpiar Historial de Chat"):
        st.session_state.messages = []
        st.rerun()

# Interfaz de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if query := st.chat_input("¿Qué quieres saber de tus documentos?"):
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # Permitir consulta si la DB está en sesión o existe en disco
    if "vector_db" in st.session_state or os.path.exists(config.CHROMA_PATH):
        try:
            with st.spinner("Consultando..."):
                qa = get_qa_chain()
                response = qa.invoke({"input": query})
                answer = response["answer"]
                sources = response["context"]
                
                st.session_state.messages.append({"role": "assistant", "content": answer})
                with st.chat_message("assistant"):
                    st.write(answer)
                    with st.expander("Ver fuentes consultadas"):
                        for doc in sources:
                            st.info(f"Fuente: {doc.metadata.get('source')} \n\nContenido: {doc.page_content[:200]}...")
        except Exception as e:
            st.error(f"Error al consultar el índice: {e}")
    else:
        st.warning("Por favor, indexa los documentos primero desde la barra lateral.")