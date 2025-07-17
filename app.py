# app.py

import streamlit as st
import os
import tempfile
from rag_pipeline.file_loader import read_txt, read_pdf, read_docx
from rag_pipeline.chroma_manager import ChromaManager
from rag_pipeline.rag_chain import RAGChain

# 初始化 ChromaManager
cm = ChromaManager()

st.set_page_config(page_title="RAG 中文問答系統", layout="wide")
st.title("📄 RAG 中文問答系統 (智能對話版)")

# 初始化會話狀態
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vectorstore_ready" not in st.session_state:
    st.session_state.vectorstore_ready = False
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# 側邊欄 - 檔案上傳
with st.sidebar:
    st.header("📁 文件上傳")
    uploaded_file = st.file_uploader("上傳文件", type=["txt", "pdf", "docx"])
    
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # 根據檔案類型讀取內容
        content = None
        if uploaded_file.type == "text/plain":
            content = read_txt(tmp_path)
        elif uploaded_file.type == "application/pdf":
            content = read_pdf(tmp_path)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            content = read_docx(tmp_path)
        else:
            st.warning("不支援的檔案格式。")

        if content:
            with st.spinner("正在處理文件..."):
                chunks = cm.split_text(content)
                st.info(f"共切出 {len(chunks)} 個文本片段")
                
                cm.add_texts(chunks)
                st.session_state.vectorstore_ready = True
                
                # 記錄已上傳的檔案
                file_info = {
                    "name": uploaded_file.name,
                    "type": uploaded_file.type,
                    "size": len(content)
                }
                if file_info not in st.session_state.uploaded_files:
                    st.session_state.uploaded_files.append(file_info)
                
                st.success("✅ 文件已成功載入！可以開始對話了。")

        os.remove(tmp_path)

    # 顯示已上傳的檔案
    if st.session_state.uploaded_files:
        st.header("📋 已上傳檔案")
        for i, file_info in enumerate(st.session_state.uploaded_files):
            st.write(f"📄 {file_info['name']}")
        
        # 清空所有資料按鈕
        if st.button("🗑️ 清空所有資料"):
            st.session_state.messages = []
            st.session_state.uploaded_files = []
            st.session_state.vectorstore_ready = False
            # 清空 ChromaDB
            import shutil
            if os.path.exists("./chroma_db"):
                shutil.rmtree("./chroma_db")
            st.rerun()

    # 對話管理
    st.header("💬 對話管理")
    
    # 顯示對話統計
    if st.session_state.messages:
        user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
        assistant_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        st.write(f"👤 使用者問題：{user_messages} 個")
        st.write(f"🤖 AI 回答：{assistant_messages} 個")
    
    # 清空對話記錄按鈕
    if st.button("🗑️ 清空對話記錄"):
        st.session_state.messages = []
        st.rerun()

# 主要對話區域
st.header("💬 智能對話")

# 創建一個容器來顯示對話歷史，支援滾動
chat_container = st.container()

# 檢查是否有向量庫
if not st.session_state.vectorstore_ready:
    st.info("👆 請先在左側上傳文件以開始對話")
else:
    # 使用者輸入
    if prompt := st.chat_input("請輸入您的問題..."):
        # 添加使用者訊息
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 生成回答
        with st.spinner("🤔 正在思考中..."):
            vs = cm.get_vectorstore()
            rag = RAGChain(vs)
            result = rag.query(prompt)
            
            # 格式化回答
            answer = result['result']
            
            # 添加參考來源
            if result.get("source_documents"):
                answer += "\n\n---\n**📚 參考來源：**\n"
                for i, doc in enumerate(result["source_documents"][:3], 1):
                    # 截取前100個字符作為摘要
                    summary = doc.page_content[:100] + "..." if len(doc.page_content) > 100 else doc.page_content
                    answer += f"{i}. {summary}\n"
            
            # 添加助手訊息到對話歷史
            st.session_state.messages.append({"role": "assistant", "content": answer})

# 在容器中顯示所有對話歷史
with chat_container:
    if st.session_state.messages:
        # 使用 CSS 來創建可滾動的對話區域
        st.markdown("""
        <style>
        .chat-container {
            max-height: 600px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 10px;
            background-color: #f9f9f9;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # 顯示對話歷史
        for i, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # 為每條訊息添加編號
                st.caption(f"訊息 {i+1}")

# 頁腳資訊
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
    💡 提示：您可以上傳多個文件，系統會整合所有內容來回答您的問題<br>
    💬 對話記錄會自動保存，您可以滾動查看之前的問答
</div>
""", unsafe_allow_html=True)
