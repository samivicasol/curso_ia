import os
from langchain_community.document_loaders import (
    PyPDFLoader, 
    Docx2txtLoader, 
    TextLoader, 
    CSVLoader
)

def load_documents(directory):
    """Carga archivos compatibles del directorio especificado."""
    documents = []
    if not os.path.exists(directory):
        os.makedirs(directory)
        return documents

    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if file.endswith('.pdf'):
            loader = PyPDFLoader(path)
        elif file.endswith('.docx'):
            loader = Docx2txtLoader(path)
        elif file.endswith('.txt'):
            loader = TextLoader(path, encoding='utf-8')
        elif file.endswith('.csv'):
            loader = CSVLoader(path)
        else:
            continue
        documents.extend(loader.load())
    return documents