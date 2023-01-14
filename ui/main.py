# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QToolBar, QToolButton, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 160, 58, 16))
        self.oldWord = QLineEdit(self.centralwidget)
        self.oldWord.setObjectName(u"oldWord")
        self.oldWord.setGeometry(QRect(150, 160, 151, 21))
        self.newWord = QLineEdit(self.centralwidget)
        self.newWord.setObjectName(u"newWord")
        self.newWord.setGeometry(QRect(430, 160, 131, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 160, 58, 16))
        self.choosePath = QToolButton(self.centralwidget)
        self.choosePath.setObjectName(u"choosePath")
        self.choosePath.setGeometry(QRect(520, 50, 31, 22))
        self.pathName = QLineEdit(self.centralwidget)
        self.pathName.setObjectName(u"pathName")
        self.pathName.setGeometry(QRect(150, 50, 351, 21))
        self.pathName.setReadOnly(True)
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(300, 210, 100, 32))
        self.showLog = QTextBrowser(self.centralwidget)
        self.showLog.setObjectName(u"showLog")
        self.showLog.setGeometry(QRect(30, 260, 741, 271))
        self.newName = QLineEdit(self.centralwidget)
        self.newName.setObjectName(u"newName")
        self.newName.setGeometry(QRect(430, 110, 131, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 110, 58, 16))
        self.oldName = QLineEdit(self.centralwidget)
        self.oldName.setObjectName(u"oldName")
        self.oldName.setGeometry(QRect(150, 110, 151, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 110, 71, 16))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(mainWindow)
        self.toolBar.setObjectName(u"toolBar")
        mainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(mainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        mainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u521b\u5efa\u65b0\u7684\u4f53\u7cfb\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u627e\u6587\u672c", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u66ff\u6362\u4e3a", None))
        self.choosePath.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.start.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u66ff\u6362\u4e3a", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u627e\u6587\u4ef6\u540d", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("mainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("mainWindow", u"toolBar_2", None))
    # retranslateUi

