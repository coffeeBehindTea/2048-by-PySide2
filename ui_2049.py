# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/dada2/Desktop/all/不创建打不开图片的python作品集/界面部分/2048/2049.ui',
# licensing of 'C:/Users/dada2/Desktop/all/不创建打不开图片的python作品集/界面部分/2048/2049.ui' applies.
#
# Created: Tue Sep  5 20:26:39 2023
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 89, 631, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb16.setAlignment(QtCore.Qt.AlignCenter)
        self.lb16.setObjectName("lb16")
        self.gridLayout.addWidget(self.lb16, 3, 3, 1, 1)
        self.lb14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb14.setAlignment(QtCore.Qt.AlignCenter)
        self.lb14.setObjectName("lb14")
        self.gridLayout.addWidget(self.lb14, 3, 1, 1, 1)
        self.lb15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb15.setAlignment(QtCore.Qt.AlignCenter)
        self.lb15.setObjectName("lb15")
        self.gridLayout.addWidget(self.lb15, 3, 2, 1, 1)
        self.lb5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb5.setObjectName("lb5")
        self.gridLayout.addWidget(self.lb5, 1, 0, 1, 1)
        self.lb13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb13.setAlignment(QtCore.Qt.AlignCenter)
        self.lb13.setObjectName("lb13")
        self.gridLayout.addWidget(self.lb13, 3, 0, 1, 1)
        self.lb9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb9.setObjectName("lb9")
        self.gridLayout.addWidget(self.lb9, 2, 0, 1, 1)
        self.lb1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setObjectName("lb1")
        self.gridLayout.addWidget(self.lb1, 0, 0, 1, 1)
        self.lb2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb2.setObjectName("lb2")
        self.gridLayout.addWidget(self.lb2, 0, 1, 1, 1)
        self.lb3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb3.setObjectName("lb3")
        self.gridLayout.addWidget(self.lb3, 0, 2, 1, 1)
        self.lb4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb4.setObjectName("lb4")
        self.gridLayout.addWidget(self.lb4, 0, 3, 1, 1)
        self.lb6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb6.setObjectName("lb6")
        self.gridLayout.addWidget(self.lb6, 1, 1, 1, 1)
        self.lb7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb7.setStyleSheet("")
        self.lb7.setAlignment(QtCore.Qt.AlignCenter)
        self.lb7.setObjectName("lb7")
        self.gridLayout.addWidget(self.lb7, 1, 2, 1, 1)
        self.lb8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb8.setAlignment(QtCore.Qt.AlignCenter)
        self.lb8.setObjectName("lb8")
        self.gridLayout.addWidget(self.lb8, 1, 3, 1, 1)
        self.lb10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb10.setAlignment(QtCore.Qt.AlignCenter)
        self.lb10.setObjectName("lb10")
        self.gridLayout.addWidget(self.lb10, 2, 1, 1, 1)
        self.lb11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb11.setObjectName("lb11")
        self.gridLayout.addWidget(self.lb11, 2, 2, 1, 1)
        self.lb12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lb12.setAlignment(QtCore.Qt.AlignCenter)
        self.lb12.setObjectName("lb12")
        self.gridLayout.addWidget(self.lb12, 2, 3, 1, 1)
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(30, 20, 611, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.score.setFont(font)
        self.score.setObjectName("score")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "MainWindow", None, -1))
        self.lb16.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb14.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb15.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb5.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb13.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb9.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb1.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb2.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb3.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb4.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb6.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb7.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb8.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb10.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb11.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.lb12.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.score.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
