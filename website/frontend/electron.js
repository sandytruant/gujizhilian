const path = require('path');
const { app, BrowserWindow, ipcMain } = require('electron');

function createWindow() {
    const win = new BrowserWindow({
        center: true,
        title: '古籍智联',
        // frame: true,
        // vibrancy: 'under-window',
        visualEffectState: 'active',
        // titleBarStyle: 'hidden',
        // trafficLightPosition: { x: 15, y: 10 },
        width: 450,
        height: 800,
        minWidth: 450,
        minHeight: 800,
        autoHideMenuBar: true,
        icon: path.join(__dirname, 'build/logo.ico'),
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false, // 允许使用 IPC
        },
    });

    // 加载本地 HTML 文件
    win.loadFile(path.join(__dirname, 'build', 'index.html')); // 这里根据你的构建路径调整
    win.removeMenu();  // 删除菜单栏
    // 监听拖动事件
    ipcMain.on('start-drag', () => {
        win.startDrag();
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

app.on('certificate-error', (event, webContents, url, error, certificate, callback) => {
    // 阻止默认行为
    event.preventDefault();
    // 信任该证书
    callback(true);
  });
