# rag_pipeline/chroma_manager.py

import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .config import *

class ChromaManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={"device": "cpu"}
        )
        if os.path.exists(PERSIST_DIRECTORY):
            self.vectorstore = Chroma(
                persist_directory=PERSIST_DIRECTORY,
                embedding_function=self.embeddings
            )
        else:
            self.vectorstore = None

    def split_text(self, text):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        return splitter.split_text(text)

    def add_texts(self, texts):
        docs = [Document(page_content=t) for t in texts]
        if os.path.exists(PERSIST_DIRECTORY):
            vs = Chroma(
                persist_directory=PERSIST_DIRECTORY,
                embedding_function=self.embeddings
            )
            vs.add_documents(docs)
            vs.persist()
            self.vectorstore = vs
        else:
            vs = Chroma.from_documents(
                docs,
                self.embeddings,
                persist_directory=PERSIST_DIRECTORY
            )
            vs.persist()
            self.vectorstore = vs

    def get_vectorstore(self):
        return self.vectorstore
