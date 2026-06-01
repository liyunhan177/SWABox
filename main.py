from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QMessageBox)
from PySide6.QtCore import Qt, QSettings
import webbrowser as web
from lib.page import *
from lib.package import *
import sys
import os

class MainWindow(QMainWindow, MainPage.Ui_MainPage, ConsentPage.Ui_ConsentPage):
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

    def GoOssierBtnClicked(self):
        web.open("https://github.com/liyunhan177/SWABox/issues/new")

class ConsentDialog(QDialog):
    def __init__(self, parent=None):
        super(ConsentDialog, self).__init__(parent)
        self.ui = ConsentPage.Ui_ConsentPage()
        self.ui.setupUi(self)
        self.ui.Yes.clicked.connect(self.accept)
        self.ui.No.clicked.connect(self.reject_and_close)

    def reject_and_close(self):
        self.reject()
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    network = WifiDet.NetworkStatus()
    wifi_states = network.is_internet_connected()

    if not wifi_states:
        print("No Internet Connection.")
        QMessageBox.critical(None, "无网络连接", "将无法使用下载与网页跳转功能\n仅可使用本地功能\n请确保您的设备处于联网状态")
    else:
        print("Internet Connected.")

    config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(config_dir, exist_ok=True)
    config_file = os.path.join(config_dir, "config.ini")
    settings = QSettings(config_file, QSettings.Format.IniFormat)
    consent_accepted = settings.value("consent_accepted", False, type=bool)

    if not consent_accepted:
        consent_dialog = ConsentDialog()
        result = consent_dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            settings.setValue("consent_accepted", True)
            settings.sync()
        else:
            sys.exit(0)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())