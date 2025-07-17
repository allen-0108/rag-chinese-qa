# 📄 RAG 中文問答系統

一個基於 RAG (Retrieval-Augmented Generation) 技術的智能中文問答系統，支援多種文件格式，提供專業的繁體中文對話體驗。

## ✨ 功能特色

### 🔍 **智能文件處理**
- 支援多種文件格式：`.txt`、`.pdf`、`.docx`
- 自動文本分割和向量化
- 使用專門的中文 embedding 模型 (BAAI/bge-base-zh)

### 💬 **智能對話系統**
- 專業的繁體中文 prompt 設計
- 對話式回答，親切自然
- 保留完整對話歷史
- 可滾動查看之前的問答記錄

### 🎯 **精準檢索**
- 向量相似度檢索
- 基於檢索內容的準確回答
- 顯示參考來源，增加可信度

### 🎨 **現代化界面**
- Streamlit 打造的直觀界面
- 側邊欄文件管理
- 對話統計和歷史管理
- 響應式設計

## 🚀 快速開始

### 環境需求
- Python38+
- Ollama (本地 LLM 服務)

### 安裝步驟

1. **克隆專案**
```bash
git clone https://github.com/allen-0108/rag-chinese-qa.git
cd rag-chinese-qa
```
2**創建虛擬環境**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate     # Windows
```

3. **安裝依賴**
```bash
pip install -r requirements.txt
```
4 **啟動 Ollama 服務**
```bash
# 安裝 Ollama (如果還沒安裝)
# 參考: https://ollama.ai/download

# 下載並啟動模型
ollama pull phi4:custom
ollama serve
```

5. **啟動應用**
```bash
streamlit run app.py
```
6**開啟瀏覽器**
訪問 `http://localhost:8501`

## 📖 使用說明

### 1. 上傳文件
- 在左側邊欄點擊「上傳文件」
- 支援 `.txt`、`.pdf`、`.docx` 格式
- 系統會自動處理並載入到向量資料庫

###2. 開始對話
- 在對話框中輸入您的問題
- 系統會基於上傳的文件內容回答
- 可以進行連續對話

### 3. 管理對話
- 查看對話統計
- 清空對話記錄
- 清空所有資料（包括文件）

## 🏗️ 專案結構

```
rag-chinese-qa/
├── app.py                 # 主應用程式
├── requirements.txt       # Python 依賴
├── README.md             # 專案說明
├── .gitignore            # Git 忽略文件
├── rag_pipeline/         # RAG 核心模組
│   ├── config.py         # 配置設定
│   ├── file_loader.py    # 文件讀取器
│   ├── chroma_manager.py # ChromaDB 管理器
│   └── rag_chain.py      # RAG 鏈
└── chroma_db/            # 向量資料庫 (自動生成)
```

## ⚙️ 配置說明

### 模型配置 (`rag_pipeline/config.py`)
```python
PERSIST_DIRECTORY = ./chroma_db"      # 向量資料庫路徑
CHUNK_SIZE = 300                       # 文本分割大小
CHUNK_OVERLAP = 50                     # 分割重疊大小
EMBEDDING_MODEL_NAME = BAAI/bge-base-zh # 中文 embedding 模型
OLLAMA_MODEL_NAME = phi4:custom      # LLM 模型名稱
OLLAMA_BASE_URL = http://localhost:11434 Ollama 服務地址
```

### 自定義配置
您可以根據需要調整以下參數：
- `CHUNK_SIZE`：調整文本分割大小
- `CHUNK_OVERLAP`：調整分割重疊
- `OLLAMA_MODEL_NAME`：更換其他 Ollama 模型

## 🔧 技術架構

### 核心技術
- **LangChain**：RAG 框架
- **ChromaDB**：向量資料庫
- **Streamlit**：Web 界面
- **Ollama**：本地 LLM 服務
- **BAAI/bge-base-zh**：中文 embedding 模型

### RAG 流程1. **文件處理**：讀取 → 分割 → 向量化
2 **檢索**：問題向量化 → 相似度檢索
3. **生成**：檢索結果 → Prompt → LLM 回答

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 開發環境設置
1 Fork 專案
2. 創建功能分支


### 代碼規範
- 使用繁體中文註釋
- 遵循 PEP 8代碼風格
- 添加適當的錯誤處理

## 📝 更新日誌

### v1.00 (202401XX)
- ✅ 支援多種文件格式 (TXT, PDF, DOCX)
- ✅ 智能中文對話系統
- ✅ 對話歷史保留功能
- ✅ 現代化 Web 界面
- ✅ 向量檢索和 RAG 實現

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 LICENSE(LICENSE) 文件

## 🙏 致謝

- [LangChain](https://github.com/langchain-ai/langchain) - RAG 框架
- [ChromaDB](https://github.com/chroma-core/chroma) - 向量資料庫
- [Streamlit](https://github.com/streamlit/streamlit) - Web 應用框架
- [Ollama](https://github.com/ollama/ollama) - 本地 LLM 服務
- [BAAI/bge-base-zh](https://huggingface.co/BAAI/bge-base-zh) - 中文 embedding 模型

## 📞 聯絡資訊

如有問題或建議，請透過以下方式聯絡：
- 提交 GitHub Issue
- Email: allen82099010@gmail.com

---

⭐ 如果這個專案對您有幫助，請給我們一個 Star！ 