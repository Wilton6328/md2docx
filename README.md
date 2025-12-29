# Markdown Universal Converter

## 📋 專案簡介
一個具備圖形化介面（GUI）的桌面工具，可將 Markdown (.md) 檔案轉換為 **Word (.docx)** 或 **PDF (.pdf)** 格式。

## ✨ 核心特點

### Word 轉換
1. **原生樣式映射**：將 Markdown 元素完美對應到 Word 內建標準樣式
2. **無自定義樣式**：嚴格使用 Word 內建樣式庫（Heading 1-6, Normal, List Bullet, List Number, Quote, Table Grid）
3. **完整格式支援**

### PDF 轉換 🆕
1. **繁體中文支援**：使用 Microsoft JhengHei 字體，完美顯示中文
2. **美觀樣式**：專業 CSS 排版，支援表格、程式碼區塊、列表等
3. **高品質輸出**：A4 尺寸，適合列印與分享

### 支援的 Markdown 語法
- ✅ 標題 (H1-H6)
- ✅ 清單（有序/無序，支援巢狀）
- ✅ 粗體、斜體、行內程式碼
- ✅ 表格
- ✅ 程式碼區塊
- ✅ 引用
- ✅ 水平線
- ✅ 圖片（僅 PDF）

## 🛠️ 技術架構

### 技術選型
- **程式語言**：Python 3.8+
- **GUI 框架**：CustomTkinter（現代化介面）
- **Word 轉換**：python-docx（精確樣式控制）
- **PDF 轉換**：markdown + weasyprint（HTML/CSS 渲染）
- **路徑處理**：pathlib（跨平台支援）

### Word vs PDF 對比

| 特性 | Word (.docx) | PDF (.pdf) |
|------|--------------|------------|
| 可編輯性 | ✅ 可編輯 | ❌ 只讀 |
| 中文支援 | ✅ | ✅ |
| 圖片支援 | ❌ | ✅ |
| 樣式控制 | 內建樣式 | CSS 自訂 |
| 檔案大小 | 較大 | 較小 |
| 適用場景 | 文件編輯 | 分享/列印 |
| 額外依賴 | 無 | GTK3 (Windows) |

## 📦 安裝步驟

### 1. 安裝 Python
確保已安裝 Python 3.8 或更高版本：
```bash
python --version
```

### 2. 安裝依賴套件

#### 基本安裝（僅 Word 轉換）
```bash
pip install customtkinter python-docx packaging
```

#### 完整安裝（含 PDF 轉換）
```bash
pip install -r requirements.txt
```

### 3. Windows 用戶額外步驟（PDF 功能）

> **注意**：Word 轉換無需此步驟，可直接使用！

如需 PDF 功能，需安裝 GTK3 運行時：

1. 下載：https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
2. 安裝並重啟命令提示字元
3. 詳細說明：參考 [`WINDOWS_PDF_SETUP.md`](WINDOWS_PDF_SETUP.md)

**macOS/Linux**：無需額外步驟，直接安裝依賴即可。

## 🚀 使用方法

### 啟動程式
```bash
python md_to_word_converter.py
```

或使用批次檔（Windows）：
```bash
啟動轉換器.bat
```

### 操作步驟
1. 點擊「瀏覽」選擇 Markdown 檔案
2. **選擇輸出格式**：Word (.docx) 或 PDF (.pdf)
3. （選填）自訂輸出位置，預設會在相同目錄生成
4. 點擊「開始轉換」
5. 轉換完成後可選擇立即開啟檔案

### 無 GTK3 時的行為

如果未安裝 GTK3：
- ✅ 程式正常啟動
- ✅ Word 轉換完全可用
- ⚠️ PDF 選項顯示為「PDF (.pdf) [Not Available - GTK3 Required]」
- ⚠️ 選擇 PDF 格式會提示安裝指南

## 🏗️ 架構說明

### 核心類別

#### `MarkdownToWordConverter`
Word 轉換引擎，負責：
- 解析 Markdown 語法
- 建立 Word 文件
- 映射到 Word 內建樣式

#### `MarkdownToPdfConverter` 🆕
PDF 轉換引擎，負責：
- Markdown → HTML 轉換
- 套用 CSS 樣式
- 生成高品質 PDF

#### `App`
GUI 應用程式類別，負責：
- 建立使用者介面
- 處理檔案選擇
- 格式選擇（Word/PDF）
- 顯示轉換狀態

### 樣式映射表

#### Word 轉換

| Markdown | Word 樣式 | 說明 |
|----------|----------|------|
| `# H1` | Heading 1 | 一級標題 |
| `## H2` | Heading 2 | 二級標題 |
| ` ...` | Heading 3-6 | 其他標題 |
| 段落 | Normal | 標準段落 |
| `- 列表` | List Bullet | 無序列表 |
| `1. 列表` | List Number | 有序列表 |
| `> 引用` | Quote | 引用 |
| 表格 | Table Grid | 表格 |
| `**粗體**` | Bold | 粗體 |
| `*斜體*` | Italic | 斜體 |
| `` `code` `` | Courier New | 程式碼 |

#### PDF 轉換

使用專業 CSS 樣式：
- 標題：漸層大小 + 底線
- 程式碼：灰色背景 + 等寬字體
- 表格：藍色標題 + 斑馬條紋
- 引用：左側藍色邊框

## 🔧 錯誤處理

程式包含完整的錯誤處理機制：

1. **檔案不存在**：檢查輸入檔案
2. **權限問題**：捕捉寫入錯誤
3. **編碼問題**：UTF-8 支援中文路徑
4. **依賴缺失**：優雅降級（PDF 功能不可用時）
5. **格式錯誤**：詳細錯誤訊息

## 📝 測試範例

專案包含完整測試檔案：

```bash
# 測試 Word 轉換
python test_converter.py

# 測試 PDF 轉換（需 GTK3）
python test_pdf_converter.py
```

## 📚 文件導覽

- **[README.md](README.md)** - 本文件（專案總覽）
- **[QUICKSTART.md](QUICKSTART.md)** - 5分鐘快速入門
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - 技術架構詳解
- **[PDF_FEATURE.md](PDF_FEATURE.md)** - PDF 功能說明
- **[WINDOWS_PDF_SETUP.md](WINDOWS_PDF_SETUP.md)** - Windows GTK3 安裝指南
- **[SUMMARY.md](SUMMARY.md)** - 專案交付總結

## ⚠️ 注意事項

### 不支援的 Markdown 語法
- 註腳
- 任務列表 `- [ ]`
- LaTeX 數學公式

### 系統需求
- Python 3.8+
- Windows/macOS/Linux
- 對於 PDF 功能：GTK3 運行時（Windows）

### Word 版本相容性
產生的 .docx 檔案相容：
- Microsoft Word 2007+
- LibreOffice Writer
- Google Docs
- macOS Pages

## 📦 專案結構

```
md2docx/
├── .github/
│   └── workflows/          # GitHub Actions 工作流程
├── md_to_word_converter.py # 主程式（支援 Word + PDF）
├── test_converter.py       # Word 轉換測試
├── test_pdf_converter.py   # PDF 轉換測試
├── requirements.txt        # 生產環境依賴
├── requirements-dev.txt    # 開發環境依賴
├── *.md                    # 完整文件
└── 啟動轉換器.bat          # Windows 快速啟動
```

## 🛠️ 開發者指南

### 本地開發環境

```bash
# 1. Clone repository
git clone https://github.com/yourusername/md2docx.git
cd md2docx

# 2. 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt -r requirements-dev.txt

# 4. 執行測試
pytest

# 5. 代碼格式化
black .
```

### 本地構建執行檔

```bash
# 使用 PyInstaller 打包
pyinstaller --name md2docx --onefile --windowed md_to_word_converter.py

# 輸出: dist/md2docx.exe (Windows) 或 dist/md2docx (macOS/Linux)
```

## 🔄 版本歷史

### v2.0 (2025-12-30) 🆕
- ✨ 新增 PDF 轉換功能
- ✨ 繁體中文完整支援
- ✨ 優雅降級處理（無 GTK3 時）
- 📝 完整文件更新

### v1.0 (2025-12-29)
- 🎉 初版發布
- ✅ Word 轉換功能
- ✅ 內建樣式映射
- ✅ GUI 介面

## 📄 授權
MIT License

## 👤 作者
Antigravity - 資深軟體架構師團隊

## 🙏 致謝

- **python-docx** - Word 文件處理
- **weasyprint** - PDF 生成
- **CustomTkinter** - 現代化 GUI
- **markdown** - Markdown 解析

---

**⭐ 如果這個專案對您有幫助，請給我們一個 Star！**
