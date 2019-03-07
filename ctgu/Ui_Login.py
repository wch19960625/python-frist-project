# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\py1.0\Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import pickle



def show_code(dome):
    try:
        with open('save_code.kpl', 'rb') as fl:
            data = pickle.load(fl)
        fl.close()
        data = dict(data)
        # print(data)
    except:
        data = {}
    if len(data) != 0:
        var_usr_name0 = data['usr_name']
        var_usr_pwd0 = data['usr_pwd']
    else:
        var_usr_name0 = ''
        var_usr_pwd0 = ''
    if dome == 1:
        return var_usr_name0
    else:
        return var_usr_pwd0

def button_chlick(dome):
    try:
        with open('save_dome.kpl', 'rb') as fl:
            data = pickle.load(fl)
        fl.close()
        data = dict(data)
        #print(data)
    except:
        data ={'psd':'False','atom':'False'}
        pass
    if dome == 1:
        return data['psd']
        #print(data['psd'])
    elif dome == 2 :
        return data['atom']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 297)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 461, 351))
        self.label.setStyleSheet("image: url(:/frist/image/bg_login.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 130, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(show_code(1))
        self.lineEdit.setStyleSheet('''QLineEdit{background-color: rgba(255, 255, 255, 30%);border:1px solid #b9babb;}''')
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 170, 201, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(show_code(2))
        self.lineEdit_2.setStyleSheet('''QLineEdit{background-color: rgba(255, 255, 255, 30%);border:1px solid #b9babb;}''')
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(120, 200, 201, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(eval(button_chlick(1)))
        if button_chlick(1) == 'True':
            self.checkBox.toggle()
            self.checkBox.toggle()
        self.horizontalLayout_4.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setChecked(eval(button_chlick(2)))
        if button_chlick(2) == 'True':
            self.checkBox_2.toggle()
            self.checkBox_2.toggle()
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(120, 240, 201, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.setStyleSheet('''QPushButton {background-color: rgba(255, 255, 255, 50%);border:1px solid #b9babb;}''')
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(426, 4, 21, 21))
        self.pushButton_2.setStyleSheet("border-image: url(:/frist/image/ext.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 0, 31, 31))
        self.pushButton_3.setStyleSheet("border-image: url(:/frist/image/min.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "教务助手"))
        self.label_2.setText(_translate("MainWindow", "学号："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.checkBox_2.setText(_translate("MainWindow", "自动登录"))
        self.pushButton.setText(_translate("MainWindow", "登录"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

import login01_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

