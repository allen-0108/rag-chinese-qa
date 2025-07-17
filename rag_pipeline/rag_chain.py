# rag_pipeline/rag_chain.py

from langchain_community.llms.ollama import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from .config import *

class RAGChain:
    def __init__(self, vectorstore):
        self.llm = Ollama(
            model=OLLAMA_MODEL_NAME,
            base_url=OLLAMA_BASE_URL,
            temperature=0.7
        )
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        # 自定義繁體中文 prompt 模板
        self.prompt_template = PromptTemplate(
            input_variables=["context", "question"],
            template="""你是一位專業且友善的 AI 助理。請根據以下提供的參考資料來回答使用者的問題。

參考資料：
{context}

使用者問題：{question}

請遵循以下指導原則：
1. 使用繁體中文回答
2. 回答要專業、準確且易懂
3. 如果參考資料中有相關資訊，請基於這些資訊回答
4. 如果參考資料中沒有足夠資訊，請誠實說明並提供一般性的建議，或提及沒有相關資訊
5. 使用對話式的語氣，讓回答更親切自然
6. 結構化回答，使用適當的段落和重點標示
7. 避免過於冗長的回答，保持簡潔明瞭

請開始回答："""
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt_template}
        )

    def query(self, question):
        result = self.qa_chain(question)
        return result
