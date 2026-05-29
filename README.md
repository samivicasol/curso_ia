# RAG Agent con Streamlit y Groq

Este proyecto implementa un agente basado en Retrieval-Augmented Generation (RAG) que permite consultar documentos locales (PDF, DOCX, TXT y CSV) mediante lenguaje natural utilizando la API de Groq.

## Objetivo

Construir un asistente capaz de responder preguntas utilizando documentos internos almacenados en un directorio local, con actualización frecuente.

## Arquitectura

El sistema sigue un enfoque RAG estándar dividido en dos fases:

Fase de indexación:
Documentos -> fragmentación -> embeddings -> almacenamiento en base vectorial

Fase de consulta:
Pregunta -> embedding -> recuperación de contexto -> generación con LLM

## Stack tecnológico

- Lenguaje: Python
- LLM: Groq (LLaMA3)
- Interfaz: Streamlit
- Base vectorial: ingFace
- Procesamiento de documentos:
  - PDF: pypdf
  - DOCX: python-docx
  - TXT: nativo
  - CSV: pandas

## Estructura del proyecto

rag-streamlit-groq/

- data/
- app.py
- rag_pipeline.py
- document_loader.py
- config.py
- requirements.txt
- README.md

## Instalación
**En Windows (PowerShell):**

> **Nota:** Si recibes un error de ejecución de scripts, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

```powershell
# 1. Crea el entorno virtual
python -m venv venv
# 2. Activa el entorno virtual
.\venv\Scripts\Activate.ps1
# 3. Instala las dependencias
python -m pip install -r requirements.txt
```

## Configuración

Crear archivo .env:

```dotenv
GROQ_API_KEY=tu_api_key_de_groq
```

streamlit
langchain
langchain-text-splitters
langchain-community
langchain-pinecone
pypdf
python-docx
pandas
sentence-transformers
groq
python-dotenv

## Carga de documentos

Implementar loaders para PDF, DOCX, TXT y CSV usando LangChain.

## Fragmentación

Utilizar RecursiveCharacterTextSplitter con chunk_size 1000 y overlap 200.

## Base vectorial

Usar Pinecone como base de datos vectorial en la nube.

## Pipeline RAG

1. Buscar documentos similares
2. Construir contexto
3. Enviar prompt a Groq
4. Generar respuesta

## Interfaz

Aplicación Streamlit con entrada de texto para preguntas.

## Actualización

Reindexar documentos cuando haya cambios.

## Buenas prácticas

- Limitar número de resultados (k=5)
- Usar metadatos
- Controlar tamaño del contexto

## Casos de uso

- Soporte IT
- Consulta de documentación
- Análisis de logs

## Ejecución

### Opción A: Con activación de entorno
.\venv\Scripts\Activate.ps1
python -m streamlit run app.py

### Opción B: Ejecución directa (sin activar)
C:\copilot_rag\venv\Scripts\python.exe -m streamlit run C:\copilot_rag\app.py
