# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Python\VideoPlay\View\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(597, 403)
        LoginWindow.setMinimumSize(QtCore.QSize(330, 200))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_id = QtWidgets.QLabel(self.centralwidget)
        self.lbl_id.setObjectName("lbl_id")
        self.horizontalLayout_2.addWidget(self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id.setObjectName("txt_id")
        self.horizontalLayout_2.addWidget(self.txt_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password.setObjectName("lbl_password")
        self.horizontalLayout_3.addWidget(self.lbl_password)
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_3.addWidget(self.txt_password)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout_4.addWidget(self.btn_reset)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_login.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_4.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setObjectName("lbl_status")
        self.horizontalLayout_5.addWidget(self.lbl_status)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.lbl_id.setText(_translate("LoginWindow", "ID:"))
        self.lbl_password.setText(_translate("LoginWindow", "Password:"))
        self.btn_reset.setText(_translate("LoginWindow", "Reset"))
        self.btn_login.setText(_translate("LoginWindow", "Login"))
        self.lbl_status.setText(_translate("LoginWindow", "Message"))