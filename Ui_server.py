# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Document\Code\Python\final\server.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 510)
        MainWindow.setMinimumSize(QtCore.QSize(750, 510))
        MainWindow.setMaximumSize(QtCore.QSize(750, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Black★RockShooter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{\n"
"    background-image: url(:/background.webp);\n"
"}\n"
"#addr_lineEdit{\n"
"    padding-left:20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(20,196,188);\n"
"    border-radius:15px;\n"
"}\n"
"#com_lineEdit{\n"
"    padding-left:20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(20,196,188);\n"
"    border-radius:15px;\n"
"}\n"
"#addr_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#com_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#config_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#recv_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#getID_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#server_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#status_label{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    font: 10pt \"微软雅黑\";\n"
"}\n"
"#status_button{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#ready_button{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#ready_button:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#ready_button:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#server_switch{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#server_switch:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#server_switch:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#getID_switch{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#getID_switch:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#getID_switch:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#recv_switch{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#recv_switch:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#recv_switch:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#clear_button{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#clear_button:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#clear_button:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#send_button{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#send_button:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#send_button:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#deepLearning_start{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#deepLearning_start:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#deepLearning_start:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#deepLearning_open{\n"
"    font: 10pt \"微软雅黑\";\n"
"    color: #2f3640;\n"
"    background-color: #f5f6fa;\n"
"    border-color: #2f3640;\n"
"    border-radius: 15px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    padding: 5px;\n"
"}\n"
"#deepLearning_open:hover{\n"
"    color: #FFFFFF;\n"
"    background-color: #718093;\n"
"    border-color: #2f3640;\n"
"}\n"
"#deepLearning_open:pressed{\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #273c75, stop:1 #487eb0);\n"
"}\n"
"#send_lineEdit{\n"
"    padding-left:20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(20,196,188);\n"
"    border-radius:15px;\n"
"}\n"
"#meso_textBrowser{\n"
"    border-image: url(:/sensei.webp);\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addr_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addr_lineEdit.setGeometry(QtCore.QRect(560, 40, 151, 31))
        self.addr_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.addr_lineEdit.setText("")
        self.addr_lineEdit.setObjectName("addr_lineEdit")
        self.com_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.com_lineEdit.setGeometry(QtCore.QRect(560, 80, 151, 31))
        self.com_lineEdit.setObjectName("com_lineEdit")
        self.addr_label = QtWidgets.QLabel(self.centralwidget)
        self.addr_label.setGeometry(QtCore.QRect(510, 40, 41, 31))
        self.addr_label.setObjectName("addr_label")
        self.com_label = QtWidgets.QLabel(self.centralwidget)
        self.com_label.setGeometry(QtCore.QRect(510, 80, 41, 31))
        self.com_label.setObjectName("com_label")
        self.config_label = QtWidgets.QLabel(self.centralwidget)
        self.config_label.setGeometry(QtCore.QRect(600, 10, 71, 31))
        self.config_label.setObjectName("config_label")
        self.ready_button = QtWidgets.QPushButton(self.centralwidget)
        self.ready_button.setGeometry(QtCore.QRect(580, 120, 111, 31))
        self.ready_button.setObjectName("ready_button")
        self.server_switch = QtWidgets.QPushButton(self.centralwidget)
        self.server_switch.setGeometry(QtCore.QRect(70, 40, 60, 30))
        self.server_switch.setObjectName("server_switch")
        self.getID_switch = QtWidgets.QPushButton(self.centralwidget)
        self.getID_switch.setGeometry(QtCore.QRect(70, 80, 60, 30))
        self.getID_switch.setObjectName("getID_switch")
        self.recv_switch = QtWidgets.QPushButton(self.centralwidget)
        self.recv_switch.setGeometry(QtCore.QRect(70, 120, 60, 30))
        self.recv_switch.setObjectName("recv_switch")
        self.server_label = QtWidgets.QLabel(self.centralwidget)
        self.server_label.setGeometry(QtCore.QRect(10, 40, 61, 31))
        self.server_label.setObjectName("server_label")
        self.getID_label = QtWidgets.QLabel(self.centralwidget)
        self.getID_label.setGeometry(QtCore.QRect(20, 80, 50, 30))
        self.getID_label.setObjectName("getID_label")
        self.recv_label = QtWidgets.QLabel(self.centralwidget)
        self.recv_label.setGeometry(QtCore.QRect(20, 120, 50, 30))
        self.recv_label.setObjectName("recv_label")
        self.meso_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.meso_textBrowser.setGeometry(QtCore.QRect(10, 340, 180, 160))
        self.meso_textBrowser.setObjectName("meso_textBrowser")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(200, 470, 71, 30))
        self.clear_button.setObjectName("clear_button")
        self.send_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.send_lineEdit.setGeometry(QtCore.QRect(10, 230, 180, 30))
        self.send_lineEdit.setObjectName("send_lineEdit")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(200, 230, 71, 30))
        self.send_button.setObjectName("send_button")
        self.deepLearning_start = QtWidgets.QPushButton(self.centralwidget)
        self.deepLearning_start.setGeometry(QtCore.QRect(190, 40, 93, 31))
        self.deepLearning_start.setObjectName("deepLearning_start")
        self.deepLearning_open = QtWidgets.QPushButton(self.centralwidget)
        self.deepLearning_open.setGeometry(QtCore.QRect(190, 120, 93, 31))
        self.deepLearning_open.setObjectName("deepLearning_open")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JakaGUI"))
        self.com_lineEdit.setText(_translate("MainWindow", "12345"))
        self.addr_label.setText(_translate("MainWindow", "地址"))
        self.com_label.setText(_translate("MainWindow", "端口"))
        self.config_label.setText(_translate("MainWindow", "参数设置"))
        self.ready_button.setText(_translate("MainWindow", "CONFIRM"))
        self.server_switch.setText(_translate("MainWindow", "ON"))
        self.getID_switch.setText(_translate("MainWindow", "ON"))
        self.recv_switch.setText(_translate("MainWindow", "ON"))
        self.server_label.setText(_translate("MainWindow", "服务端"))
        self.getID_label.setText(_translate("MainWindow", "监听"))
        self.recv_label.setText(_translate("MainWindow", "接收"))
        self.clear_button.setText(_translate("MainWindow", "CLEAR"))
        self.send_button.setText(_translate("MainWindow", "SEND"))
        self.deepLearning_start.setText(_translate("MainWindow", "dSTART"))
        self.deepLearning_open.setText(_translate("MainWindow", "dOPEN"))
import image_rc
