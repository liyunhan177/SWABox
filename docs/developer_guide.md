# 开发者指南

## 核心流程走读

```python
# main.py 中的典型交互流程
class MainWindow(QMainWindow, MainPage.Ui_MainPage):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings.clicked.connect(self.SettingsBtnClicked)
        self.EMGTool.clicked.connect(self.EMGToolBtnClicked)

    def SettingsBtnClicked(self):
        self.settings_dialog = QDialog()
        self.settings_ui = Settings.Ui_settings()
        self.settings_ui.setupUi(self.settings_dialog)
        self.settings_ui.GoIssue.clicked.connect(self.GoOssierBtnClicked)
        self.settings_dialog.show()

    def EMGToolBtnClicked(self):
        self.EMG_dialog = QDialog()
        self.EMG_ui = EMGToolPage.Ui_EMGToolPage()
        self.EMG_ui.setupUi(self.EMG_dialog)
        self.EMG_ui.GoExplorer.clicked.connect(self.GoExplorBtnClicked)
        self.EMG_dialog.show()

    def GoExplorBtnClicked(self):
        OpenExplorer.open_tool_folder()
```

这个流程展示了用户点击按钮到打开新界面的完整过程：
1. 用户点击按钮触发信号
2. 创建新的 QDialog 实例
3. 加载对应的 UI 文件
4. 连接按钮信号到槽函数
5. 显示对话框

**扩展点**：如需添加新功能，可以在 `lib/page/` 下创建新的页面类，然后在 `main.py` 中添加对应的按钮点击事件处理函数。

## 如何添加一个新的界面模块

最快实现方式：
1. 使用 Qt Designer 创建新的 .ui 文件，保存到 `res/UI/` 目录
2. 使用 `pyside6-uic res/UI/YourPage.ui -o lib/page/YourPage.py` 生成对应的 Python 文件
3. 在 `lib/page/__init__.py` 中添加导入：`from .YourPage import *`
4. 在 `main.py` 的 MainWindow 类中添加按钮点击事件处理函数
5. 在处理函数中创建并显示新界面

可以先实现功能，后续再优化结构。

## 测试如何运行

目前项目没有配置自动化测试框架，建议手动测试 GUI 交互流程。提 PR 前请确保自己添加的代码至少手动验证过：

1. 界面能正常显示
2. 按钮点击有预期响应
3. 新增的功能不会影响现有功能

如果需要添加单元测试，可以使用 Python 内置的 `unittest` 模块或 `pytest`。测试文件可以放在 `tests/` 目录下。

## 高危区域

`lib/package/WifiDet.py` 涉及网络检测逻辑，不兼容的改动可能导致程序启动时误判网络状态，影响用户使用体验。如需修改网络检测逻辑，请先讨论方案。

`SWABox.spec` 是打包配置文件，错误的修改可能导致打包失败或打包后的程序缺少关键文件。修改前请备份原文件，并在多个 Windows 版本上测试打包结果。

`Tool/` 目录下的工具文件是第三方工具，不要随意修改或删除，这些工具在紧急情况下可能救命。如果需要更新工具，请在 issue 中说明原因和替换方案。