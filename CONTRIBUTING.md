# 貢獻指南

感謝您對 RAG 中文問答系統的關注！我們歡迎所有形式的貢獻。

## 如何貢獻

### 1. 報告問題 (Bug Report)
如果您發現了問題，請：
- 使用 GitHub Issues 提交問題
- 詳細描述問題的步驟
- 提供錯誤訊息和截圖
- 說明您的環境（作業系統、Python 版本等）

### 2. 功能請求 (Feature Request)
如果您有新的功能想法，請：
- 使用 GitHub Issues 提交請求
- 詳細描述功能需求
- 說明使用場景和價值

### 3. 代碼貢獻 (Code Contribution)

#### 開發環境設置1. Fork 本專案
2. 克隆您的 Fork：
   ```bash
   git clone https://github.com/your-username/rag-chinese-qa.git
   cd rag-chinese-qa
   ```3創建功能分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```4安裝開發依賴：
   ```bash
   pip install -r requirements.txt
   ```

#### 代碼規範
- 使用繁體中文註釋
- 遵循 PEP 8 代碼風格
- 函數和類別要有文檔字串
- 添加適當的錯誤處理

#### 提交變更1測試您的變更：
   ```bash
   streamlit run app.py
   ```
2. 提交變更：
   ```bash
   git add .
   git commit -m feat: 添加新功能描述"
   ```3推送到您的 Fork：
   ```bash
   git push origin feature/your-feature-name
   ```
4 發起 Pull Request

###4. 文檔貢獻
- 改進 README.md
- 添加使用範例
- 翻譯文檔
- 修正錯別字

## 提交訊息規範

使用以下格式：
- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文檔更新
- `style:` 代碼格式調整
- `refactor:` 重構代碼
- `test:` 測試相關
- `chore:` 構建過程或輔助工具的變動

範例：
```
feat: 添加 Word 文件支援
fix: 修正對話記錄清空問題
docs: 更新安裝說明
```

## 行為準則

- 尊重所有貢獻者
- 保持友善和專業的交流
- 歡迎新手提問
- 提供建設性的回饋

## 聯絡方式

如有問題，請透過以下方式聯絡：
- GitHub Issues
- Email: your-email@example.com

感謝您的貢獻！ 