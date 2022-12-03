from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QLabel
from UI_developer import *
from changepassword_controller import *
from Sqlite import *
import sys
sys.path.append("..")


class developer_controller(QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Developer()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btm_continue.clicked.connect(self.developer)

    def developer(self):
        if self.verify_login_info():
            self.close()
            self.main = changepassword_controller()
            self.main.show()
        else:
            self.ui.txt_result.setText("User Name, Password Error!")
            print("error")

    def verify_login_info(self):
        self.processSqlite = sqlite_engine()
        self.processSqlite.getTxt(
            self.ui.txt_developer.text(), self.ui.txt_dev_password.text())
        if self.processSqlite.query_dev():
            return True
        else:
            return False

