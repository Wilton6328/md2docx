# Markdown Universal Converter - 使用說明

## 功能更新

新增 **PDF 轉換功能**！現在支援：

- ✅ **Markdown → Word (.docx)** - 使用 Word 內建樣式
- ✅ **Markdown → PDF (.pdf)** - 支援繁體中文顯示

## 安裝新依賴

```bash
pip install markdown weasyprint
```

或重新安裝所有依賴：

```bash
pip install -r requirements.txt
```

## 使用方法

1. **選擇檔案**：點擊「瀏覽」或拖曳 .md 檔案
2. **選擇格式**：選擇輸出格式（Word 或 PDF）
3. **開始轉換**：點擊「開始轉換」按鈕
4. **查看結果**：轉換完成後可直接開啟檔案

## PDF 特色

### 繁體中文支援
- 使用 Microsoft JhengHei 字體
- 完美顯示中文內容，無亂碼

### 美觀樣式
- 專為 A4 頁面優化
- 支援表格、程式碼區塊、列表等
- 標題自動分級顯示

### 支援的 Markdown 語法

| 語法 | Word | PDF |
|------|------|-----|
| 標題 H1-H6 | ✅ | ✅ |
| 粗體/斜體 | ✅ | ✅ |
| 列表（有序/無序） | ✅ | ✅ |
| 程式碼區塊 | ✅ | ✅ |
| 表格 | ✅ | ✅ |
| 引用 | ✅ | ✅ |
| 水平線 | ✅ | ✅ |
| 圖片 | ❌ | ✅* |

*PDF 支援圖片，但需要圖片路徑可訪問

## 技術細節

### Word 轉換
- 引擎：python-docx
- 特點：嚴格使用 Word 內建樣式（Heading 1-6, Normal, List Bullet 等）

### PDF 轉換
- 引擎：markdown + weasyprint
- 特點：
  - HTML/CSS 渲染引擎
  - 支援中文字體
  - 支援圖片嵌入
  - 高品質 PDF 輸出

## 常見問題

### Q: 安裝 weasyprint 失敗？

**Windows**：weasyprint 需要 GTK3 運行時。如果安裝失敗，請：

1. 下載 GTK3：https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
2. 安裝後重試 `pip install weasyprint`

**macOS/Linux**：通常可以直接安裝，無需額外步驟。

### Q: PDF 中文顯示不正常？

確保系統已安裝 Microsoft JhengHei 字體（Windows 預設有）。

### Q: 如何只安裝 Word 轉換功能？

如果不需要 PDF 功能，可以只安裝：
```bash
pip install customtkinter python-docx packaging
```

然後修改程式碼移除 PDF 相關導入。

## 啟動程式

```bash
python md_to_word_converter.py
```

或使用批次檔：
```bash
啟動轉換器.bat
```

---

**版本**：2.0  
**更新日期**：2025-12-30
