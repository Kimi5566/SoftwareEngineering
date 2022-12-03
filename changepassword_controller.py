from UI_changepassword import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QLabel
from Sqlite import *
import sys

class changepassword_controller(QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_changepasswordwindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btm_continue.clicked.connect(self.updatepassword)

    def updatepassword(self):
        self.processSqlite = sqlite_engine()
        self.processSqlite.getTxt(self.ui.txt_email.text(), self.ui.txt_new_password.text())
        if self.processSqlite.update():
            self.ui.txt_result.setText("password update successful,please use new password login")
        else:
             self.ui.txt_result.setText("password update Fail")