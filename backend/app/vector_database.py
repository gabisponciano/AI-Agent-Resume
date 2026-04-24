from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

pasta = "teste"

# def load_docs():
#       load_docs = PyPDFDirectoryLoader(pasta, glob = "*.pdf")
#       docs = load_docs.load()
#       return docs

def chunks_particioner(docs):
      separetor = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap= 500,
            length_function = len,
            add_start_index = True
      )
      chunks = separetor.split_documents(docs)
      return chunks

def vectorize_chunks(chunks):
      db = Chroma.from_documents(chunks, OllamaEmbeddings(model="nomic-embed-text"), persist_directory="vector_db")
      print("Database was created!")
       

# def create_db():
#       docs = load_docs()
#       print(docs)
#       chunks = chunks_particioner(docs)
#       vectorize_chunks(chunks)

# create_db()