const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// 提供靜態文件服務
app.use(express.static(__dirname));

// 確保 robots.txt 和 sitemap.xml 可以被訪問
app.get('/robots.txt', (req, res) => {
  res.sendFile(path.join(__dirname, 'robots.txt'));
});

app.get('/sitemap.xml', (req, res) => {
  res.set('Content-Type', 'text/xml');
  res.sendFile(path.join(__dirname, 'sitemap.xml'));
});

// 所有其他路由都返回 index.html（用於單頁應用）
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

