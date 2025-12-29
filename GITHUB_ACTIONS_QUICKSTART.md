# 快速入門指南 - GitHub Actions 部署

本文件提供最快速的方式開始使用 GitHub Actions 自動化部署。

## ⚡ 5 分鐘快速開始

### 步驟 1: 確認檔案已就緒

確認以下檔案已存在於專案中：

```
✅ pyproject.toml
✅ requirements.txt
✅ requirements-dev.txt
✅ .gitignore
✅ .github/workflows/ci.yml
✅ .github/workflows/release.yml
```

### 步驟 2: 推送到 GitHub

```bash
# 初始化 Git（如已初始化可跳過）
git init
git branch -M main

# 添加所有檔案
git add .
git commit -m "feat: 添加 GitHub Actions CI/CD 配置"

# 建立 GitHub Repository 並推送
# 請先在 GitHub 建立新的 repository
git remote add origin https://github.com/yourusername/md2docx.git
git push -u origin main
```

### 步驟 3: 查看 CI 執行結果

1. 前往 GitHub Repository
2. 點擊 **Actions** 標籤
3. 查看 "CI - 持續整合" 工作流程
4. 確認所有測試通過 ✅

### 步驟 4: 建立第一個 Release

```bash
# 確認版本號（pyproject.toml 中應為 1.0.0）
# 建立並推送標籤
git tag -a v1.0.0 -m "首次正式發布"
git push origin v1.0.0
```

### 步驟 5: 下載執行檔

1. 等待約 5-10 分鐘讓 GitHub Actions 完成構建
2. 前往 **Releases** 頁面
3. 下載對應平台的執行檔並測試

🎉 **完成！** 您的專案現在已具備自動化 CI/CD 能力！

---

## 📋 日常開發流程

### 提交代碼（觸發 CI）

```bash
# 1. 進行開發
# 2. 提交變更
git add .
git commit -m "feat: 添加新功能"
git push

# → 自動觸發 CI 測試
```

### 發布新版本（觸發 Release）

```bash
# 1. 更新 pyproject.toml 中的版本號
# 2. 提交並打標籤
git add pyproject.toml
git commit -m "chore: bump version to 1.1.0"
git tag v1.1.0
git push origin main
git push origin v1.1.0

# → 自動構建並發布到 Releases
```

---

## 🔧 常見自訂需求

### 修改測試的 Python 版本

編輯 `.github/workflows/ci.yml`：

```yaml
matrix:
  python-version: ['3.9', '3.10', '3.11']  # 移除不需要的版本
```

### 修改測試的作業系統

```yaml
matrix:
  os: [ubuntu-latest, windows-latest]  # 移除 macos-latest 節省時間
```

### 添加圖示（Icon）

1. 建立 `icon.ico` 檔案（Windows 圖示）
2. 放置在專案根目錄
3. GitHub Actions 會自動使用它

### 跳過 CI 測試

在 commit message 中加入 `[skip ci]`：

```bash
git commit -m "docs: 更新文件 [skip ci]"
```

---

## ❓ 疑難排解

### CI 失敗：找不到模組

**問題**：`ModuleNotFoundError: No module named 'xxx'`

**解決**：
```bash
# 確認依賴已加入 requirements.txt
echo "missing-package==1.0.0" >> requirements.txt
git add requirements.txt
git commit -m "fix: 添加遺漏的依賴"
git push
```

### Release 失敗：PyInstaller 錯誤

**問題**：打包時找不到模組或檔案

**解決**：編輯 `.github/workflows/release.yml`：

```yaml
# 添加隱藏的依賴
pyinstaller --name md2docx \
  --onefile \
  --hidden-import=customtkinter \
  --hidden-import=docx \
  md_to_word_converter.py
```

### 日誌查看

前往 **Actions** → 點擊失敗的工作流程 → 展開步驟查看詳細錯誤訊息。

---

## 📚 延伸閱讀

- 詳細部署指南：[DEPLOYMENT.md](DEPLOYMENT.md)
- 完整專案說明：[README.md](README.md)
- 架構文件：[ARCHITECTURE.md](ARCHITECTURE.md)

---

**需要更多協助？** 請查看 [GitHub Actions 官方文件](https://docs.github.com/en/actions) 或在 Issues 中提問。
