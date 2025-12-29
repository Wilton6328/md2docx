# Markdown to Word Converter - 技術架構文件

## 目錄
1. [架構概覽](#架構概覽)
2. [核心設計原則](#核心設計原則)
3. [樣式映射機制](#樣式映射機制)
4. [程式碼結構](#程式碼結構)
5. [關鍵技術實作](#關鍵技術實作)

---

## 架構概覽

### 系統架構圖

```
┌─────────────────────────────────────────┐
│         使用者介面層 (GUI)               │
│    CustomTkinter - 現代化圖形介面         │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│         應用程式邏輯層                    │
│    - 檔案選擇與驗證                       │
│    - 狀態管理與錯誤處理                   │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│      轉換引擎層 (Core Logic)             │
│    MarkdownToWordConverter               │
│    - Markdown 解析                       │
│    - Word 文件生成                       │
│    - 樣式映射                            │
└────────────────┬────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────┐
│         底層套件層                       │
│    - python-docx (Word 處理)             │
│    - pathlib (路徑處理)                  │
│    - re (正則表達式)                     │
└─────────────────────────────────────────┘
```

---

## 核心設計原則

### 1. 使用 Word 內建樣式（無自定義樣式）

**為什麼這很重要？**

- **相容性**：確保在不同 Word 版本中都能正確顯示
- **一致性**：使用者可以用自己的 Word 模板快速調整格式
- **標準化**：符合企業文件標準

**如何實現？**

```python
# ✅ 正確：使用內建樣式
para = self.doc.add_paragraph(style='Normal')
heading = self.doc.add_heading(level=1)  # 自動使用 Heading 1
list_item = self.doc.add_paragraph(style='List Bullet')

# ❌ 錯誤：建立自定義樣式
# styles = document.styles
# custom_style = styles.add_style('MyCustomStyle', WD_STYLE_TYPE.PARAGRAPH)
```

### 2. 完整的錯誤處理

```python
try:
    # 檔案操作
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
except FileNotFoundError:
    raise Exception(f"找不到檔案: {md_path}")
except PermissionError:
    raise Exception(f"沒有權限寫入檔案: {docx_path}")
except Exception as e:
    raise Exception(f"轉換過程發生錯誤: {str(e)}")
```

### 3. 跨平台路徑處理

```python
from pathlib import Path

# 自動處理 Windows/macOS/Linux 路徑差異
base_path = Path(filename)
output_full_path = base_path.parent / output_filename
```

---

## 樣式映射機制

### Word 內建樣式列表

| 樣式名稱 | Word 內部名稱 | 用途 |
|---------|--------------|------|
| Heading 1 | `Heading 1` | 一級標題 |
| Heading 2 | `Heading 2` | 二級標題 |
| Heading 3 | `Heading 3` | 三級標題 |
| Heading 4 | `Heading 4` | 四級標題 |
| Heading 5 | `Heading 5` | 五級標題 |
| Heading 6 | `Heading 6` | 六級標題 |
| Normal | `Normal` | 一般段落 |
| List Bullet | `List Bullet` | 項目符號列表 |
| List Number | `List Number` | 編號列表 |
| Quote | `Quote` | 引用段落 |
| Table Grid | `Table Grid` | 表格 |

### 映射實作

#### 1. 標題映射

```python
def _process_heading(self, line: str):
    heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
    if heading_match:
        level = len(heading_match.group(1))  # 計算 # 的數量
        text = heading_match.group(2)
        
        # add_heading() 自動使用對應的 Heading N 樣式
        para = self.doc.add_heading(level=level)
        para.text = text
```

**技術細節：**
- `add_heading(level=1)` → 使用 `Heading 1` 樣式
- `add_heading(level=2)` → 使用 `Heading 2` 樣式
- 以此類推...

#### 2. 列表映射

```python
def _add_list_item(self, text: str, indent: int, is_ordered: bool):
    # 根據列表類型選擇樣式
    style = 'List Number' if is_ordered else 'List Bullet'
    para = self.doc.add_paragraph(style=style)
    
    # 設定縮排層級（不是修改樣式）
    level = indent // 2
    para.paragraph_format.left_indent = Inches(0.5 * level)
```

**重要觀念：**
- 使用 `paragraph_format` 調整格式 ≠ 建立新樣式
- 這只是調整現有樣式的參數

#### 3. 表格映射

```python
def _create_table(self, rows_data):
    table = self.doc.add_table(rows=len(rows_data), cols=len(rows_data[0]))
    
    # 使用 Word 內建的 Table Grid 樣式
    table.style = 'Table Grid'
    
    # 填入資料...
```

#### 4. 行內格式映射

```python
def _apply_inline_formatting(self, paragraph, text: str):
    # 粗體
    if is_bold:
        run.bold = True  # 設定屬性，不建立樣式
    
    # 斜體
    if is_italic:
        run.italic = True
    
    # 程式碼
    if is_code:
        run.font.name = 'Courier New'
        run.font.size = Pt(10)
```

**關鍵區別：**
```python
# ✅ 正確：修改 run 屬性
run.bold = True
run.font.name = 'Courier New'

# ❌ 錯誤：建立字元樣式
# char_style = styles.add_style('CodeStyle', WD_STYLE_TYPE.CHARACTER)
# run.style = char_style
```

---

## 程式碼結構

### 主要類別與方法

```
MarkdownToWordConverter (轉換引擎)
│
├── convert()                      # 主要轉換入口
│
├── _process_line()                # 處理單行 Markdown
│   ├── 標題處理
│   ├── 列表處理
│   ├── 表格處理
│   ├── 程式碼區塊處理
│   ├── 引用處理
│   └── 一般段落處理
│
├── _add_list_item()               # 新增列表項目
├── _apply_inline_formatting()     # 套用行內格式
├── _parse_inline_formatting()     # 解析行內格式
├── _process_table()               # 處理表格
├── _process_code_block()          # 處理程式碼區塊
└── _add_horizontal_line()         # 新增水平線

App (GUI 應用程式)
│
├── __init__()                     # 初始化視窗
├── _create_widgets()              # 建立 UI 元件
├── browse_file()                  # 選擇輸入檔案
├── browse_output()                # 選擇輸出位置
└── convert_file()                 # 執行轉換
```

---

## 關鍵技術實作

### 1. Markdown 解析

#### 正則表達式模式

```python
# 標題
r'^(#{1,6})\s+(.+)$'
# 範例：### Title → 群組1='###', 群組2='Title'

# 無序列表
r'^(\s*)[*\-+]\s+(.+)$'
# 範例：  - Item → 群組1='  ', 群組2='Item'

# 有序列表
r'^(\s*)\d+\.\s+(.+)$'
# 範例：  1. Item → 群組1='  ', 群組2='Item'

# 行內格式
r'(`[^`]+`|\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*]+\*)'
# 匹配：`code`, ***bold italic***, **bold**, *italic*
```

#### 行內格式解析流程

```python
def _parse_inline_formatting(self, text: str):
    """
    將文字分割為多個片段，每個片段標記其格式
    
    輸入：  "This is **bold** and *italic* text"
    輸出：  [
              ("This is ", False, False, False),
              ("bold", True, False, False),
              (" and ", False, False, False),
              ("italic", False, True, False),
              (" text", False, False, False)
            ]
    """
    result = []
    # ... 使用正則表達式分割與標記 ...
    return result
```

### 2. 表格處理

```python
def _process_table(self, lines: list, start_index: int):
    # 步驟 1：收集表格行
    table_lines = []
    while '|' in lines[i]:
        table_lines.append(lines[i])
        i += 1
    
    # 步驟 2：解析表格資料
    rows = []
    for line in table_lines:
        # 跳過分隔線 (|---|---|)
        if re.match(r'^\|[\s\-:]+\|$', line.strip()):
            continue
        
        # 分割儲存格
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        rows.append(cells)
    
    # 步驟 3：建立 Word 表格
    table = self.doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = 'Table Grid'  # 使用內建樣式
    
    # 步驟 4：填入資料
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_data in enumerate(row_data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.text = cell_data
            
            # 第一列粗體（標題）
            if row_idx == 0:
                for run in cell.paragraphs[0].runs:
                    run.bold = True
```

### 3. 程式碼區塊處理

```python
def _process_code_block(self, lines: list, start_index: int):
    # 收集 ``` 之間的所有行
    code_lines = []
    i = start_index + 1
    while i < len(lines) and not lines[i].strip().startswith('```'):
        code_lines.append(lines[i])
        i += 1
    
    # 建立段落
    code_text = '\n'.join(code_lines)
    para = self.doc.add_paragraph(style='Normal')
    run = para.add_run(code_text)
    
    # 設定等寬字型
    run.font.name = 'Courier New'
    run.font.size = Pt(10)
    
    # 新增淺灰色背景
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), 'F0F0F0')
    para._element.get_or_add_pPr().append(shading_elm)
```

### 4. 水平線處理

```python
def _add_horizontal_line(self, paragraph):
    """使用段落邊框實現水平線"""
    p = paragraph._element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    
    # 底部邊框
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')    # 單線
    bottom.set(qn('w:sz'), '6')          # 粗細
    bottom.set(qn('w:space'), '1')       # 間距
    bottom.set(qn('w:color'), 'auto')    # 顏色
    
    pBdr.append(bottom)
    pPr.append(pBdr)
```

---

## 環境獨立性設計

### 1. 編碼處理

```python
# 明確使用 UTF-8 編碼
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()
```

**支援：**
- 中文檔案名稱
- 中文路徑
- 中文內容

### 2. 路徑處理

```python
from pathlib import Path

# 跨平台路徑處理
base_path = Path(filename)
output_filename = base_path.stem + ".docx"
output_full_path = base_path.parent / output_filename
```

**優點：**
- 自動處理 Windows 的反斜線與 Unix 的斜線
- 正確處理含空白的路徑
- 提供方便的路徑操作方法

### 3. Word 相容性

```python
from docx import Document

# 建立的 .docx 檔案相容：
# - Word 2007+
# - LibreOffice Writer
# - Google Docs
# - macOS Pages
```

---

## 效能考量

### 1. 逐行處理

```python
lines = md_content.split('\n')
for i, line in enumerate(lines):
    self._process_line(line, lines, i)
```

**優點：**
- 記憶體使用可控（不需一次載入整份文件結構）
- 可處理大型 Markdown 檔案

### 2. 正則表達式編譯

雖然目前未實作，但可優化如下：

```python
class MarkdownToWordConverter:
    def __init__(self):
        # 預先編譯正則表達式
        self.heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
        self.list_pattern = re.compile(r'^(\s*)[*\-+]\s+(.+)$')
        # ...
```

---

## 未來擴充方向

### 1. 支援更多 Markdown 語法

- [ ] 註腳
- [ ] 任務列表 (`- [ ]`)
- [ ] 定義列表
- [ ] LaTeX 數學公式（需要 MathML）
- [ ] 圖片嵌入

### 2. 批次轉換

```python
def batch_convert(self, input_dir: str, output_dir: str):
    """批次轉換資料夾中的所有 .md 檔案"""
    for md_file in Path(input_dir).glob('*.md'):
        output_file = Path(output_dir) / f"{md_file.stem}.docx"
        self.convert(str(md_file), str(output_file))
```

### 3. 自訂 Word 模板

```python
def convert(self, md_path: str, docx_path: str, template_path: str = None):
    if template_path:
        self.doc = Document(template_path)  # 使用自訂模板
    else:
        self.doc = Document()  # 使用預設模板
```

### 4. 進度回報

```python
def convert(self, md_path: str, docx_path: str, progress_callback=None):
    total_lines = len(lines)
    for i, line in enumerate(lines):
        self._process_line(line, lines, i)
        if progress_callback:
            progress_callback(i + 1, total_lines)
```

---

## 測試策略

### 單元測試範例

```python
import unittest

class TestMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MarkdownToWordConverter()
    
    def test_heading_parsing(self):
        """測試標題解析"""
        # 建立測試文件
        # 驗證標題樣式
        pass
    
    def test_list_parsing(self):
        """測試列表解析"""
        pass
    
    def test_table_parsing(self):
        """測試表格解析"""
        pass
```

### 整合測試

```python
def test_full_conversion(self):
    """完整轉換測試"""
    self.converter.convert('test.md', 'output.docx')
    
    # 驗證檔案存在
    assert os.path.exists('output.docx')
    
    # 驗證可正常開啟
    doc = Document('output.docx')
    assert len(doc.paragraphs) > 0
```

---

## 總結

這個 Markdown to Word Converter 的核心價值在於：

1. ✓ **嚴格使用 Word 內建樣式**，確保相容性
2. ✓ **完整的錯誤處理**，提供良好的使用體驗
3. ✓ **跨平台設計**，支援各種作業系統
4. ✓ **清晰的架構**，易於維護與擴充

透過 python-docx 的精確控制，我們能夠確保產生的 Word 文件不會引入任何自定義樣式，完美符合企業文件標準與最佳實踐。
