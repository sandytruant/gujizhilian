# Website Demo

## 内容

- 基于 Flask 的简易后端（对` search/search.py` 的修改）：`search.py`
- 基于 React.js + MUI 的前端：`frontend/`

## 运行代码

### 后端

Python >= 3.10

```bash
pip install -r requirements.txt
python search.py
```

后端服务器应该运行在 http://127.0.0.1:5000

浏览器访问 http://127.0.0.1:5000/search?query=hainei 应当有输出

### 前端

#### 安装 Node.js 

选择 v20.18.0 (LTS)，参见https://nodejs.org/en/download/package-manager

#### 运行

如果本机没有科学上网，需要设置 nodejs 为国内源。

```bash
cd frontend
npm install @mui/joy @fontsource/inter react-spring slick-carousel
./test.sh
```

可以访问 http://127.0.0.1:3000 或 https://127.0.0.1:3001 访问页面

后端服务器现可通过 https://127.0.0.1:5001 访问
