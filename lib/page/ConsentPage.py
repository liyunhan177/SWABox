# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsentPageQolzoG.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from . import main_rc

class Ui_ConsentPage(object):
    def setupUi(self, ConsentPage):
        if not ConsentPage.objectName():
            ConsentPage.setObjectName(u"ConsentPage")
        ConsentPage.resize(607, 297)
        ConsentPage.setMinimumSize(QSize(607, 297))
        ConsentPage.setMaximumSize(QSize(607, 297))
        icon = QIcon()
        icon.addFile(u":/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ConsentPage.setWindowIcon(icon)
        self.label = QLabel(ConsentPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 451, 91))
        self.label_2 = QLabel(ConsentPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 0, 171, 91))
        self.label_3 = QLabel(ConsentPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 591, 91))
        self.label_4 = QLabel(ConsentPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 591, 21))
        self.label_4.setOpenExternalLinks(True)
        self.Yes = QPushButton(ConsentPage)
        self.Yes.setObjectName(u"Yes")
        self.Yes.setGeometry(QRect(150, 250, 101, 26))
        self.No = QPushButton(ConsentPage)
        self.No.setObjectName(u"No")
        self.No.setGeometry(QRect(372, 250, 101, 26))

        self.retranslateUi(ConsentPage)
        self.No.clicked.connect(ConsentPage.close)

        QMetaObject.connectSlotsByName(ConsentPage)
    # setupUi

    def retranslateUi(self, ConsentPage):
        ConsentPage.setWindowTitle(QCoreApplication.translate("ConsentPage", u"SWABox", None))
        self.label.setText(QCoreApplication.translate("ConsentPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">\u6b22\u8fce\u4f7f\u7528</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ConsentPage", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700; color:#22c55d;\">SWABox</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ConsentPage", u"<html><head/><body><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:11pt; color:#f9fafb;\">\u5728\u5f00\u59cb\u4f7f\u7528\u672c\u5e94\u7528\u4e4b\u524d\uff0c\u5efa\u8bae\u4f60\u82b1\u51e0\u5206\u949f\u4e86\u89e3\u6211\u4eec</span><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:11pt; font-weight:700; color:#f9fafb;\">\u5982\u4f55\u5904\u7406\u4f60\u7684\u6570\u636e\uff0c\u4ee5\u53ca\u4f60\u4eab\u6709\u7684\u6743\u5229</span></p><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:11pt; font-weight:700; color:#f9fafb;\">\u4e0e\u5e94\u9075\u5b88\u7684"
                        "\u89c4\u5219\u3002</span></p><p><span style=\" font-family:'quote-cjk-patch','Inter','system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen','Ubuntu','Cantarell','Open Sans','Helvetica Neue','sans-serif'; font-size:11pt; color:#f9fafb;\">\u8bf7\u70b9\u51fb\u4e0b\u65b9\u94fe\u63a5\u9605\u8bfb\u5b8c\u6574\u7684\u6cd5\u5f8b\u6587\u4ef6\u3002</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ConsentPage", u"<html><head/><body><p align=\"center\"><a href=\"https://swabox.cc.cd/app/privacy\"><span style=\" font-size:12pt; text-decoration: underline; color:#22c55d;\">\u9690\u79c1\u653f\u7b56 </span></a><a href=\"https://swabox.cc.cd/app/terms\"><span style=\" font-size:12pt; text-decoration: underline; color:#22c55d;\">\u7528\u6237\u534f\u8bae</span></a></p></body></html>", None))
        self.Yes.setText(QCoreApplication.translate("ConsentPage", u"\u540c\u610f", None))
        self.No.setText(QCoreApplication.translate("ConsentPage", u"\u62d2\u7edd", None))
    # retranslateUi

