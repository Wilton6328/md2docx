# Markdown to Word Converter - 快速入門指南

## 🚀 5 分鐘安裝與使用

### 步驟 1：確認 Python 環境

開啟命令提示字元（CMD）或 PowerShell，執行：

```bash
python --version
```

**要求**：Python 3.8 或更高版本

如果沒有安裝 Python，請前往 [python.org](https://www.python.org/downloads/) 下載安裝。

---

### 步驟 2：安裝依賴套件

在專案目錄中執行：

```bash
pip install -r requirements.txt
```

或手動安裝：

```bash
pip install customtkinter python-docx packaging
```

**預期輸出**：
```
Successfully installed customtkinter-5.2.1 python-docx-1.1.0 packaging-25.0 darkdetect-0.8.0
```

---

### 步驟 3：運行程式

#### 方法 1：使用批次檔（推薦）

直接雙擊 **`啟動轉換器.bat`**

#### 方法 2：命令列

```bash
python md_to_word_converter.py
```

---

### 步驟 4：轉換檔案

1. 點擊 **「瀏覽」** 按鈕選擇您的 `.md` 檔案
2. （選填）設定輸出位置，或使用預設（相同目錄）
3. 點擊 **「開始轉換」**
4. 轉換完成後可選擇直接開啟 Word 檔案

---

## 🎯 測試轉換器

我們提供了一個完整的測試檔案 `test_sample.md`，您可以用它來測試轉換功能：

### 自動測試

```bash
python test_converter.py
```

**預期輸出**：
```
==================================================
Markdown to Word Converter - 功能測試
==================================================

輸入檔案: test_sample.md
輸出檔案: test_output.docx

開始轉換...

[OK] 轉換成功！
檔案大小: 39,116 bytes
段落數量: 139
表格數量: 3

==================================================
[OK] 測試通過！
==================================================
```

### 手動測試

1. 啟動程式：`python md_to_word_converter.py`
2. 選擇 `test_sample.md`
3. 點擊「開始轉換」
4. 開啟生成的 `test_sample.docx` 檢查轉換品質

---

## 📋 支援的 Markdown 語法

| 語法 | Markdown | Word 樣式 |
|------|----------|-----------|
| 標題 | `# H1` 到 `###### H6` | Heading 1-6 |
| 粗體 | `**文字**` 或 `__文字__` | Bold |
| 斜體 | `*文字*` 或 `_文字_` | Italic |
| 程式碼 | `` `code` `` | Courier New |
| 無序列表 | `- 項目` | List Bullet |
| 有序列表 | `1. 項目` | List Number |
| 表格 | `\| 欄位 \|` | Table Grid |
| 程式碼區塊 | ` ```code``` ` | Normal + 灰色背景 |
| 引用 | `> 引用` | Quote |
| 水平線 | `---` | 段落邊框 |

---

## ❓ 常見問題

### Q1: 轉換失敗，顯示 "找不到檔案"

**解決方法**：
- 確認 Markdown 檔案路徑正確
- 檢查檔案是否真的存在
- 避免使用特殊符號在檔案名稱中

### Q2: 程式無法啟動

**可能原因與解決方法**：

1. **缺少套件**
   ```bash
   pip install --upgrade customtkinter python-docx packaging
   ```

2. **Python 版本太舊**
   ```bash
   python --version  # 需要 3.8+
   ```

3. **編碼問題（Windows）**
   ```bash
   chcp 65001  # 切換為 UTF-8
   ```

### Q3: 轉換後的 Word 檔案格式不正確

**檢查項目**：
- 是否使用標準 Markdown 語法
- 表格是否有正確的分隔線
- 程式碼區塊是否有關閉的 ` ``` `

### Q4: 支援圖片嵌入嗎？

目前版本**不支援**圖片嵌入。未來版本會加入此功能。

### Q5: 可以批次轉換嗎？

目前版本僅支援單檔轉換。如需批次處理，可以使用 Python 腳本：

```python
from md_to_word_converter import MarkdownToWordConverter
from pathlib import Path

converter = MarkdownToWordConverter()
for md_file in Path('.').glob('*.md'):
    output_file = md_file.with_suffix('.docx')
    converter.convert(str(md_file), str(output_file))
    print(f'✓ 已轉換: {md_file}')
```

---

## 🔧 進階使用

### 自訂輸出模板

如果您有自己的 Word 模板：

```python
from docx import Document
from md_to_word_converter import MarkdownToWordConverter

class CustomConverter(MarkdownToWordConverter):
    def convert(self, md_path: str, docx_path: str, template_path: str = None):
        # 讀取 Markdown
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 使用自訂模板
        if template_path:
            self.doc = Document(template_path)
        else:
            self.doc = Document()
        
        # ... 其餘轉換邏輯 ...
```

### 整合到現有專案

```python
from md_to_word_converter import MarkdownToWordConverter

def your_function():
    converter = MarkdownToWordConverter()
    
    try:
        converter.convert('input.md', 'output.docx')
        print('轉換成功！')
    except Exception as e:
        print(f'錯誤：{e}')
```

---

## 📞 技術支援

### 檢查日誌

如果遇到問題，執行測試腳本以獲取詳細錯誤訊息：

```bash
python test_converter.py
```

### 驗證安裝

```bash
pip list | findstr "customtkinter python-docx packaging"
```

**預期輸出**：
```
customtkinter       5.2.1
packaging           25.0
python-docx         1.1.0
```

---

## 🎉 開始使用

現在您已經準備好了！試試轉換您的第一個 Markdown 檔案吧！

1. 執行 `python md_to_word_converter.py`
2. 選擇 `.md` 檔案
3. 點擊「開始轉換」
4. 享受完美轉換的 Word 文件！

---

**提示**：將 `啟動轉換器.bat` 建立桌面捷徑，隨時快速啟動！
