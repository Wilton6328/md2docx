# Markdown to Word 轉換測試文件

這是一個完整的測試文件，用於驗證所有支援的 Markdown 語法。

## 標題層級測試

### 三級標題
#### 四級標題
##### 五級標題
###### 六級標題

## 文字格式測試

這是一個包含多種格式的段落：

- **粗體文字**展示
- *斜體文字*展示
- ***粗斜體***展示
- `行內程式碼`展示
- 這是普通文字

## 列表測試

### 無序列表

- 第一項
- 第二項
- 第三項
  - 子項目 A
  - 子項目 B
    - 深層子項目 1
    - 深層子項目 2
- 第四項

### 有序列表

1. 第一步驟
2. 第二步驟
3. 第三步驟
   1. 子步驟 3.1
   2. 子步驟 3.2
4. 第四步驟

### 混合列表

1. 有序列表項目
   - 無序子項目
   - 另一個無序子項目
2. 下一個有序項目
   1. 有序子項目
   2. 另一個有序子項目

## 表格測試

### 基本表格

| 姓名 | 年齡 | 職業 |
|------|------|------|
| 張三 | 28 | 工程師 |
| 李四 | 35 | 設計師 |
| 王五 | 42 | 專案經理 |

### 複雜表格

| 功能 | Markdown | Word 樣式 | 狀態 |
|------|----------|-----------|------|
| 標題 | # - ###### | Heading 1-6 | ✓ |
| 列表 | - 或 1. | List Bullet/Number | ✓ |
| 表格 | \| 欄位 \| | Table Grid | ✓ |
| 程式碼 | \`\`\` | Normal + Courier | ✓ |

## 程式碼區塊測試

### Python 程式碼

```python
def convert_markdown_to_word(md_file, docx_file):
    """
    將 Markdown 轉換為 Word 文件
    """
    converter = MarkdownToWordConverter()
    converter.convert(md_file, docx_file)
    print("轉換完成！")

if __name__ == "__main__":
    convert_markdown_to_word("test.md", "output.docx")
```

### JavaScript 程式碼

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
  return `Welcome to Markdown Converter`;
}

greet("World");
```

## 引用測試

> 這是一段引用文字。
> 
> 引用可以包含多個段落。

> 這是另一段獨立的引用。

## 水平線測試

以下是水平線：

---

水平線上方的文字。

___

水平線下方的文字。

***

另一種水平線樣式。

## 複雜格式組合

這個段落包含**粗體**、*斜體*、***粗斜體***和`程式碼`的組合，用於測試行內格式是否能正確解析。

### 多層次內容

1. **第一層**：這是第一層內容
   - *子項目*：這是子項目內容
   - 另一個子項目包含`程式碼片段`
2. **第二層**：包含多種格式
   - 粗體：**重要內容**
   - 斜體：*強調內容*
   - 程式碼：`variable_name`

## 實際應用範例

### 專案結構

```
md2docx/
├── md_to_word_converter.py  # 主程式
├── requirements.txt          # 依賴套件
├── README.md                 # 說明文件
└── test_sample.md            # 測試檔案
```

### 使用步驟

1. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

2. **執行程式**
   ```bash
   python md_to_word_converter.py
   ```

3. **選擇檔案並轉換**
   - 點擊「瀏覽」選擇 .md 檔案
   - 點擊「開始轉換」

## 技術規格

| 項目 | 詳細資訊 |
|------|----------|
| Python 版本 | 3.8+ |
| 主要套件 | customtkinter, python-docx |
| 支援作業系統 | Windows, macOS, Linux |
| Word 相容性 | Word 2007+ (.docx) |

## 結論

這個測試文件涵蓋了所有支援的 Markdown 語法，包括：

- ✓ 標題（H1-H6）
- ✓ 文字格式（粗體、斜體、程式碼）
- ✓ 列表（有序、無序、巢狀）
- ✓ 表格
- ✓ 程式碼區塊
- ✓ 引用
- ✓ 水平線

---

**測試完成時間**：2025-12-29  
**版本**：1.0
