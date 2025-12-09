const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// 提供靜態文件服務
app.use(express.static(__dirname));

// 所有路由都返回 index.html（用於單頁應用）
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

