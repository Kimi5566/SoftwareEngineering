from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QLabel
from main_controller import *
from forget_controller import *
from developer_controller import *
from Sqlite import *
from UI_login import *
import sys
sys.path.append("..")


class Login_controller(QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btn_login.clicked.connect(self.display_MainForm)
        self.ui.btn_reset.clicked.connect(self.forget_MainForm)
        self.ui.btn_developer.clicked.connect(self.developer_MainForm)

    def display_MainForm(self):
        if self.verify_login_info():
            self.close()
            self.main = Main_controller()
            self.main.show()

        else:
            self.ui.lbl_status.setText("ID, Password Error!")
            print("error")

    def verify_login_info(self):
        self.processSqlite = sqlite_engine()
        self.processSqlite.getTxt(
            self.ui.txt_id.text(), self.ui.txt_password.text())
        if self.processSqlite.query():
            return True
        else:
            return False
   

    def forget_MainForm(self):
            # self.close()
            self.main = forget_controller()
            self.main.show()
    
    def developer_MainForm(self):
            self.main = developer_controller()
            self.main.show()

