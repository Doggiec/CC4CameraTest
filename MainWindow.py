# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.micTestTab = QtWidgets.QWidget()
        self.micTestTab.setObjectName("micTestTab")
        self.tabWidget.addTab(self.micTestTab, "")
        self.diskTestTab = QtWidgets.QWidget()
        self.diskTestTab.setObjectName("diskTestTab")
        self.tabWidget.addTab(self.diskTestTab, "")
        self.videoTestTab = QtWidgets.QWidget()
        self.videoTestTab.setObjectName("videoTestTab")
        self.tabWidget.addTab(self.videoTestTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.micTestTab), _translate("MainWindow", "麦克风测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diskTestTab), _translate("MainWindow", "磁盘测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.videoTestTab), _translate("MainWindow", "图像测试"))

