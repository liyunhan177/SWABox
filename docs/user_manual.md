# 用户手册

项目是一个 Python GUI 程序，**以 Windows 为主要支持平台**。Mac 和 Linux 目前处于社区测试阶段，尚未经过完整验证，欢迎尝试并反馈问题。

## 安装指南

### 方式一：使用 Windows 安装包（推荐给普通用户）

从 [https://github.com/SWABox/SWABox](https://github.com/SWABox/SWABox) 的 Releases 页面下载最新的 `.exe` 安装包（或 `.msi`、便携版压缩包）。

1. 下载后双击运行
2. 如果 Windows SmartScreen 弹出警告，点击"更多信息"然后选择"仍要运行"（这是打包工具常见的误报，并非安全问题；如果仍有顾虑，可以从源码运行）
3. 安装路径建议不要包含中文，避免潜在兼容问题
4. 如果启动后没反应，可以尝试右键以管理员身份运行

### 方式二：从源码运行（适合希望修改代码或跨平台尝试的开发者）

Windows 用户请优先使用安装包。以下源码运行方式在 Windows 上已验证，Mac/Linux 下的步骤类似，但可能遇到未预期的兼容性问题，我们非常欢迎你在这些平台上尝试并提交反馈或修复。

1. 克隆仓库：
```bash
git clone https://github.com/SWABox/SWABox.git
```

2. 安装 Python 3.10+

3. 创建虚拟环境：
- Windows: `python -m venv venv` → `venv\Scripts\activate`
- Mac/Linux: `python3 -m venv venv` → `source venv/bin/activate`

4. 安装依赖：
```bash
pip install -r requirements.txt
```

5. 运行程序：
```bash
python main.py
```

如果 `pip install` 时某些 GUI 相关包（如 `PySide6`）编译失败，可尝试使用预编译的 wheel 文件，或检查系统是否缺少 GUI 库依赖（Linux 下可能需要安装 `libxcb` 等）。具体问题欢迎在 issue 中提出，附上你的系统和完整报错。

## 常见错误和解决办法

### 错误 1：启动后窗口闪退
**现象**：双击 exe 后窗口一闪而过，程序直接退出

**解决办法**：在命令行中运行程序查看错误输出，大概率是缺少某个 DLL 或显卡驱动版本过旧。如果是源码运行，直接在终端执行 `python main.py` 查看具体报错信息。

### 错误 2：找不到模块 'lib.package.WifiDet'
**现象**：运行时提示 `ModuleNotFoundError: No module named 'lib.package.WifiDet'`

**解决办法**：确保在项目根目录下运行程序，并且 lib 目录下有对应的 Python 文件。如果是打包后的 exe，检查 `_internal` 目录下是否正确包含了 lib 目录。

### 错误 3：网络检测失败导致功能受限
**现象**：启动时提示"无网络连接"，但实际网络正常

**解决办法**：这是 `WifiDet.py` 中的网络检测机制问题。程序会尝试连接 8.8.8.8 的 53 端口，如果防火墙阻止了该连接，就会误判为无网络。可以暂时关闭防火墙或修改 `lib/package/WifiDet.py` 中的检测逻辑。

## 需要注意的操作

**不建议**把程序装在中文路径下，部分打包工具生成的 exe 对非英文路径支持不佳，可能导致资源文件加载失败。

**不建议**直接从 U 盘运行，某些依赖可能无法正确加载，特别是 PySide6 的插件文件。

**不建议**在虚拟环境中修改 `Tool` 目录下的工具文件，这些文件会在重新打包时被覆盖，建议在源码目录下进行修改。
