# GitHub Actions 部署指南

本文件說明如何使用 GitHub Actions 實現自動化測試與發布。

## 📋 前置作業

### 1. 建立 GitHub Repository

```bash
# 初始化 Git（如果尚未初始化）
git init

# 添加所有檔案
git add .
git commit -m "Initial commit"

# 連接到 GitHub
git remote add origin https://github.com/yourusername/md2docx.git
git branch -M main
git push -u origin main
```

### 2. 設定 Repository（選用）

如果需要代碼覆蓋率報告，可以設定 Codecov：

1. 前往 [Codecov](https://codecov.io/)
2. 使用 GitHub 帳號登入
3. 添加 `md2docx` repository
4. 複製 `CODECOV_TOKEN`
5. 在 GitHub Repository 中設定 Secret：
   - **Settings** → **Secrets and variables** → **Actions**
   - **New repository secret**
   - Name: `CODECOV_TOKEN`
   - Value: 貼上您的 token

## 🚀 工作流程說明

### CI 工作流程 (`.github/workflows/ci.yml`)

**觸發時機**：
- Push 到 `main` 或 `develop` 分支
- 建立 Pull Request

**執行內容**：
1. 在 Ubuntu、Windows、macOS 三個平台測試
2. 測試 Python 3.8、3.9、3.10、3.11 版本
3. 代碼格式檢查（Black）
4. 語法檢查（Flake8）
5. 單元測試（Pytest）
6. 安全性掃描（Safety & Bandit）

### Release 工作流程 (`.github/workflows/release.yml`)

**觸發時機**：
- 推送以 `v` 開頭的版本標籤（例如 `v1.0.0`、`v2.1.3`）

**執行內容**：
1. 在三個平台構建可執行檔
2. 使用 PyInstaller 打包
3. 建立 GitHub Release
4. 自動上傳所有平台的執行檔

## 📦 發布新版本

### 步驟 1：更新版本號

編輯 `pyproject.toml`：

```toml
[project]
name = "md2docx"
version = "1.0.0"  # ← 更新這裡
```

### 步驟 2：更新 CHANGELOG（建議）

建議建立 `CHANGELOG.md` 記錄變更：

```markdown
# Changelog

## [1.0.0] - 2025-12-29

### Added
- 初始版本發布
- GUI 介面
- Markdown 轉 Word 功能

### Fixed
- 修正中文路徑問題
```

### 步驟 3：提交並打標籤

```bash
# 提交所有變更
git add .
git commit -m "chore: bump version to 1.0.0"

# 建立語義化版本標籤
git tag -a v1.0.0 -m "Release version 1.0.0"

# 推送到 GitHub（標籤會觸發自動發布）
git push origin main
git push origin v1.0.0
```

### 步驟 4：監控工作流程

1. 前往 GitHub Repository 的 **Actions** 頁面
2. 查看 "Release - 自動發布" 工作流程
3. 等待所有平台構建完成（約 5-10 分鐘）

### 步驟 5：檢查 Release

1. 前往 **Releases** 頁面
2. 確認新版本已建立
3. 下載並測試各平台的執行檔

## 🔧 疑難排解

### 問題：CI 測試失敗

**解決方法**：
```bash
# 本地執行測試
pytest -v

# 檢查代碼格式
black --check .

# 檢查語法
flake8 .
```

### 問題：PyInstaller 打包失敗

**常見原因**：
- 缺少依賴套件
- 圖示檔案不存在（`icon.ico`）

**解決方法**：
- 移除 `release.yml` 中的 `--icon=icon.ico` 選項
- 或建立一個 `icon.ico` 檔案

### 問題：Release 無法建立

**可能原因**：
- 標籤格式不正確（必須是 `v*.*.*`）
- 權限不足

**解決方法**：
```bash
# 檢查標籤格式
git tag -l

# 刪除錯誤的標籤
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0

# 重新建立正確的標籤
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
```

## 🎯 最佳實踐

### 1. 語義化版本控制

遵循 [Semantic Versioning](https://semver.org/)：

- `v1.0.0` - 主要版本（重大變更）
- `v1.1.0` - 次要版本（新功能）
- `v1.1.1` - 修訂版本（錯誤修正）

### 2. 預發布版本

測試版本可使用：

```bash
git tag v1.0.0-beta.1
git push origin v1.0.0-beta.1
```

在 `release.yml` 中會自動標記為 pre-release。

### 3. 保持 CHANGELOG

每次發布前更新 `CHANGELOG.md`，讓用戶了解變更內容。

### 4. 本地測試

發布前務必本地構建與測試：

```bash
# 運行所有測試
pytest -v

# 本地打包測試
pyinstaller --name md2docx --onefile --windowed md_to_word_converter.py

# 測試執行檔
./dist/md2docx
```

## 📚 相關文件

- [GitHub Actions 文件](https://docs.github.com/en/actions)
- [PyInstaller 文件](https://pyinstaller.org/)
- [語義化版本](https://semver.org/)
- [Codecov 整合](https://docs.codecov.com/docs)

## ❓ 需要協助？

如果遇到問題，請：

1. 檢查 [GitHub Actions 日誌](https://github.com/yourusername/md2docx/actions)
2. 查看 [Issues 頁面](https://github.com/yourusername/md2docx/issues)
3. 建立新的 Issue 描述問題
