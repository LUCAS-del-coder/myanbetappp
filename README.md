# MyanCasino Clone

Myanmar Online Casino Website Clone

## 本地開發

### 安裝依賴

```bash
npm install
```

### 運行本地服務器

```bash
npm start
```

服務器將在 `http://localhost:3000` 啟動

## 部署到 Railway（透過 GitHub）

### 步驟 1: 準備 GitHub 倉庫

1. 在 GitHub 上創建一個新的倉庫（如果還沒有）
2. 初始化 Git（如果還沒有初始化）：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用戶名/你的倉庫名.git
git push -u origin main
```

### 步驟 2: 連接 Railway 到 GitHub

1. 前往 [Railway.app](https://railway.app)
2. 登入或註冊帳號
3. 點擊「New Project」
4. 選擇「Deploy from GitHub repo」
5. 授權 Railway 訪問你的 GitHub 帳號
6. 選擇你的倉庫
7. Railway 會自動偵測 `railway.json` 配置檔

### 步驟 3: 配置部署設定

Railway 會自動：
- 偵測這是一個 Node.js 專案
- 執行 `npm install` 安裝依賴
- 使用 `npm start` 啟動服務器（如 `railway.json` 中配置）
- 自動分配 PORT 環境變數

### 步驟 4: 部署完成

1. Railway 會自動開始部署
2. 部署完成後，點擊專案中的「Settings」
3. 在「Domains」區塊可以：
   - 使用 Railway 提供的免費域名（格式：`your-project.up.railway.app`）
   - 或添加自定義域名

### Railway 配置說明

`railway.json` 檔案已配置：
- **Builder**: NIXPACKS（自動偵測 Node.js 環境）
- **Start Command**: `npm start`
- **Restart Policy**: 失敗時自動重啟，最多重試 10 次

### 環境變數

目前專案使用 Railway 自動分配的 `PORT` 環境變數，無需手動配置。

## 專案結構

- `index.html` - 主 HTML 檔案
- `index-n25-25a1.css` - 樣式表
- `server.js` - Express 靜態檔案服務器
- `assets/` - 圖片和標誌資源
- `package.json` - Node.js 依賴配置
- `railway.json` - Railway 部署配置
- `.gitignore` - Git 忽略檔案配置

## 技術棧

- Node.js
- Express.js
- 靜態檔案服務

