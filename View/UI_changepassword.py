# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changepasswordwindow(object):
    def setupUi(self, changepasswordwindow):
        changepasswordwindow.setObjectName("changepasswordwindow")
        changepasswordwindow.setWindowModality(QtCore.Qt.NonModal)
        changepasswordwindow.resize(535, 340)
        changepasswordwindow.setMinimumSize(QtCore.QSize(330, 200))
        changepasswordwindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(changepasswordwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Background = QtWidgets.QFrame(self.centralwidget)
        self.Background.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0.159091 rgba(77, 99, 208, 181), stop:0.482955 rgba(49, 192, 98, 192), stop:0.9375 rgba(2, 2, 139, 190));")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Background)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Logo = QtWidgets.QFrame(self.Background)
        self.Logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Logo)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.Logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../National_Chung_Cheng_University.svg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Logo)
        self.frame_2 = QtWidgets.QFrame(self.Background)
        self.frame_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_title = QtWidgets.QLabel(self.frame_2)
        self.lbl_title.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_8.addWidget(self.lbl_title)
        self.verticalLayout.addWidget(self.frame_2)
        self.email = QtWidgets.QFrame(self.Background)
        self.email.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 127, 190);")
        self.email.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.email.setFrameShadow(QtWidgets.QFrame.Raised)
        self.email.setObjectName("email")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.email)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_enail = QtWidgets.QLabel(self.email)
        self.lbl_enail.setObjectName("lbl_enail")
        self.horizontalLayout_2.addWidget(self.lbl_enail)
        self.txt_email = QtWidgets.QLineEdit(self.email)
        self.txt_email.setObjectName("txt_email")
        self.horizontalLayout_2.addWidget(self.txt_email)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.email)
        self.frame = QtWidgets.QFrame(self.Background)
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 127, 190);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.txt_password = QtWidgets.QLabel(self.frame)
        self.txt_password.setObjectName("txt_password")
        self.horizontalLayout_9.addWidget(self.txt_password)
        self.txt_new_password = QtWidgets.QLineEdit(self.frame)
        self.txt_new_password.setObjectName("txt_new_password")
        self.horizontalLayout_9.addWidget(self.txt_new_password)
        self.btm_continue = QtWidgets.QPushButton(self.frame)
        self.btm_continue.setObjectName("btm_continue")
        self.horizontalLayout_9.addWidget(self.btm_continue)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.Background)
        self.frame_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 127, 190);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.txt_status = QtWidgets.QLabel(self.frame_3)
        self.txt_status.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_status.sizePolicy().hasHeightForWidth())
        self.txt_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_status.setFont(font)
        self.txt_status.setObjectName("txt_status")
        self.horizontalLayout_11.addWidget(self.txt_status)
        self.txt_result = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_result.setFont(font)
        self.txt_result.setText("")
        self.txt_result.setObjectName("txt_result")
        self.horizontalLayout_11.addWidget(self.txt_result)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.Background)
        changepasswordwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(changepasswordwindow)
        self.statusbar.setObjectName("statusbar")
        changepasswordwindow.setStatusBar(self.statusbar)

        self.retranslateUi(changepasswordwindow)
        QtCore.QMetaObject.connectSlotsByName(changepasswordwindow)

    def retranslateUi(self, changepasswordwindow):
        _translate = QtCore.QCoreApplication.translate
        changepasswordwindow.setWindowTitle(_translate("changepasswordwindow", "Forget Password-changepassword"))
        self.lbl_title.setText(_translate("changepasswordwindow", "Please key in your user name and new password"))
        self.lbl_enail.setText(_translate("changepasswordwindow", "Please key in your user name"))
        self.txt_password.setText(_translate("changepasswordwindow", "Please key in your new password"))
        self.btm_continue.setText(_translate("changepasswordwindow", "continue"))
        self.txt_status.setText(_translate("changepasswordwindow", "Status:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepasswordwindow = QtWidgets.QMainWindow()
    ui = Ui_changepasswordwindow()
    ui.setupUi(changepasswordwindow)
    changepasswordwindow.show()
    sys.exit(app.exec_())
