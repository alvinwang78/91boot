# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateFile.ui'
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

class Ui_createFile(object):
    def setupUi(self, createFile):
        if not createFile.objectName():
            createFile.setObjectName(u"createFile")
        createFile.resize(800, 600)
        self.centralwidget = QWidget(createFile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 58, 16))
        self.oldWord = QLineEdit(self.centralwidget)
        self.oldWord.setObjectName(u"oldWord")
        self.oldWord.setGeometry(QRect(150, 100, 113, 21))
        self.newWord = QLineEdit(self.centralwidget)
        self.newWord.setObjectName(u"newWord")
        self.newWord.setGeometry(QRect(430, 100, 113, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 100, 58, 16))
        self.chooseTemplateFolder = QToolButton(self.centralwidget)
        self.chooseTemplateFolder.setObjectName(u"chooseTemplateFolder")
        self.chooseTemplateFolder.setGeometry(QRect(520, 50, 31, 22))
        self.templateFolder = QLineEdit(self.centralwidget)
        self.templateFolder.setObjectName(u"templateFolder")
        self.templateFolder.setGeometry(QRect(150, 50, 351, 21))
        self.templateFolder.setReadOnly(True)
        self.create = QPushButton(self.centralwidget)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(300, 210, 100, 32))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 150, 81, 16))
        self.targetFolder = QLineEdit(self.centralwidget)
        self.targetFolder.setObjectName(u"targetFolder")
        self.targetFolder.setGeometry(QRect(150, 150, 351, 21))
        self.targetFolder.setReadOnly(True)
        self.chooseTargetFolder = QToolButton(self.centralwidget)
        self.chooseTargetFolder.setObjectName(u"chooseTargetFolder")
        self.chooseTargetFolder.setGeometry(QRect(520, 150, 31, 22))
        self.showLog = QTextBrowser(self.centralwidget)
        self.showLog.setObjectName(u"showLog")
        self.showLog.setGeometry(QRect(30, 260, 741, 271))
        createFile.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(createFile)
        self.statusbar.setObjectName(u"statusbar")
        createFile.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(createFile)
        self.toolBar.setObjectName(u"toolBar")
        createFile.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(createFile)
        self.toolBar_2.setObjectName(u"toolBar_2")
        createFile.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(createFile)

        QMetaObject.connectSlotsByName(createFile)
    # setupUi

    def retranslateUi(self, createFile):
        createFile.setWindowTitle(QCoreApplication.translate("createFile", u"\u521b\u5efa\u65b0\u7684\u4f53\u7cfb\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("createFile", u"\u9009\u62e9\u6a21\u7248\u76ee\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("createFile", u"\u67e5\u627e\u6587\u672c", None))
        self.label_4.setText(QCoreApplication.translate("createFile", u"\u66ff\u6362\u4e3a", None))
        self.chooseTemplateFolder.setText(QCoreApplication.translate("createFile", u"...", None))
        self.create.setText(QCoreApplication.translate("createFile", u"\u5f00\u59cb\u751f\u6210", None))
        self.label_3.setText(QCoreApplication.translate("createFile", u"\u9009\u62e9\u751f\u6210\u76ee\u5f55", None))
        self.chooseTargetFolder.setText(QCoreApplication.translate("createFile", u"...", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("createFile", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("createFile", u"toolBar_2", None))
    # retranslateUi

