# Windows 安裝 WeasyPrint 指南

## ⚠️ 重要提示

在 Windows 上使用 WeasyPrint 需要額外安裝 **GTK3 運行時庫**。

## 🔧 安裝步驟

### 方法 1：使用 GTK3 安裝器（推薦）

1. **下載 GTK3 運行時**
   - 訪問：https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
   - 下載最新的 `gtk3-runtime-x.x.x-x-x-ts-win64.exe`

2. **安裝 GTK3**
   - 運行下載的安裝程式
   - 使用預設選項完成安裝
   - **重要**：勾選「Add to PATH」選項

3. **重啟命令提示字元**
   - 關閉所有命令提示字元視窗
   - 開啟新的命令提示字元

4. **驗證安裝**
   ```bash
   python test_pdf_converter.py
   ```

### 方法 2：使用 MSYS2（進階用戶）

```bash
# 安裝 MSYS2
# https://www.msys2.org/

# 在 MSYS2 中執行
pacman -S mingw-w64-x86_64-gtk3
```

### 方法 3：使用替代方案（最簡單）

如果不想安裝 GTK3，可以使用以下替代方案：

#### 選項 A：使用 pdfkit（需要 wkhtmltopdf）

修改 PDF 轉換器：

```python
# 安裝
pip install pdfkit markdown

# 需要下載 wkhtmltopdf
# https://wkhtmltopdf.org/downloads.html

# 使用方法與 weasyprint 類似
```

#### 選項 B：使用 reportlab（純Python）

```python
# 安裝
pip install reportlab markdown

# 但中文支援需要更多配置
```

#### 選項 C：只使用 Word 轉換

如果 PDF 功能不是必需的，可以：

1. 只使用 Word 轉換功能
2. 需要 PDF 時，用 Word 另存為 PDF

## 🧪 測試安裝

安裝 GTK3 後，執行：

```bash
python -c "from weasyprint import HTML; print('✓ WeasyPrint 可用！')"
```

如果看到 "✓ WeasyPrint 可用！"，表示安裝成功。

## 🔄 故障排除

### 錯誤：cannot load library 'libgobject-2.0-0'

**原因**：未安裝 GTK3 或 PATH 未正確設定

**解決方案**：
1. 確保已安裝 GTK3
2. 重啟命令提示字元
3. 檢查環境變數 PATH 是否包含 GTK3 路徑
   - 通常是：`C:\Program Files\GTK3-Runtime Win64\bin`

### 錯誤：DLL load failed

**解決方案**：
1. 重新安裝 GTK3
2. 確保使用 64 位元版本（如果 Python 是 64 位元）
3. 重啟電腦

## 📋 完整安裝檢查清單

- [ ] 安裝 Python 3.8+
- [ ] 安裝依賴：`pip install -r requirements.txt`
- [ ] 安裝 GTK3 運行時
- [ ] 重啟命令提示字元
- [ ] 測試：`python test_pdf_converter.py`
- [ ] ✅ 成功執行

## 💡 建議

對於一般用戶：
- ✅ **Word 轉換**：直接可用，無需額外配置
- 🔧 **PDF 轉換**：需要安裝 GTK3，稍微複雜

**推薦工作流程**：
1. 先使用 Word 轉換功能
2. 如果確實需要 PDF，再安裝 GTK3

---

**需要協助？** 參考 WeasyPrint 官方文檔：
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows
