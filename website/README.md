# Website Demo

## 更新

1. **模糊匹配**：以声韵搭配 Trie 树为基础进行音节划分`SyllSeg.py`，从而实现一定的模糊匹配效果。
2. **繁简转换**：在 `../search/search.py`的基础上，对前后端进行了调整，使得简、繁查询分属不同 API，访问不同数据库。
3. **页面选择**：针对搜索结果较多的情况分页呈现，每页10条结果。
4. **出处复制**：偏好设置中可勾选“复制出处”，在 SQLite 中添加了 source 栏。另：可以按此进一步添加其他信息。
5. **页面优化**：将偏好设置收进抽屉。

后端已用 `systemctl` 部署于 CLab 服务器。

规划：尝试基于 Electron 构建 windows_amd64 发行版

## 内容

- 基于 Flask 的简易后端（对 `../search/search.py` 的修改）：`search.py`
- 基于 React.js + MUI 的前端：`frontend/`

## 说明

> [!warning] 重要事项
>
> 由于网站还在测试阶段，如果运行存在问题，可能是下面的原因。碰到问题请随时联系我！
>
> 1. 服务器处没有部署 `systemd` ，采用的是 `nohup ... &` 的方式，非常不稳定。因此打不开很可能是因为进程 Exit 了。
>    1. 如果是本地运行前端网页时无法弹出结果，那可能是云服务器的后端进程 Exit 了。
>       - 前端网页代码调用部署于云服务器的后端查询 API。如需调用本地运行的后端查询 API，请手动修改代码。
>    2. 如果访问 https://<服务器IP>:3001 不成功，那可能是云服务器的前端进程 Exit 了。
> 2. 由于（浏览器还是什么玩意儿的限制？），因为项目中涉及到一个按 Tab 键复制到剪贴板的操作，需要 https 连接。服务端采用自签名证书实现 https 连接，但自签名证书存在安全风险，各大浏览器上一般都需要**手动信任**。
>    1. 请使用 3001 端口（https 端口）访问页面。请检查：访问 3001 端口时，是否明确使用 https 协议连接（https://）
>    2. 进入网页前会有弹窗，手动点击继续访问（这意味着你已经手动信任了 https://xxx:3001 的证书）。
>    3. 经测试发现，对于 Safari 和 FireFox 浏览器，需要手动信任 https://xxx:5001 （后端查询API）的证书。

#### 工作机制阐释

用户前端输入→实时访问后端查询接口（目前代码中写的是访问 CLab 云服务器的 https 端口）→后端查询接口返回查询结果→前端呈现运行代码

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
