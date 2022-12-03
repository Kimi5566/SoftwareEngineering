from UI_forget import *
from changepassword_controller import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QLabel
import sys
import email.message
import smtplib
import time
import random

sys.path.append("..")


class forget_controller(QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_forgetpasswordwindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btn_send.clicked.connect(self.send_email)
        self.ui.btn_verify.clicked.connect(self.verify_code)

    def vcode(self):
        output= str(random.randint(0,9999)).zfill(4)
        return output

    def send_email(self):
        global vcode
        vcode=self.vcode()
        receivermailaddress = self.ui.txt_email.text()
        sendermailaddress="software.engineering718@gmail.com"
        senderpassword="useforsoftwareengineering"
        atp="vrproampgpzeeogq"
        msg=email.message.EmailMessage()


        msg["From"]=sendermailaddress
        msg["To"]=receivermailaddress
        msg["Subject"]="請確認驗證碼"


        msg.add_alternative(f"<h3>驗證碼為{vcode},請使用驗證碼進行驗證</h3>",subtype="html") 


        server=smtplib.SMTP_SSL("smtp.gmail.com",465) 
        server.login(sendermailaddress,atp)
        server.send_message(msg)
        server.close()

    def verify_code(self):
            userkeyinvcode = self.ui.txt_verification_code.text()
            if vcode == userkeyinvcode:
                self.ui.txt_result.setText("correct")
                self.main = changepassword_controller()
                self.main.show() 
                #self.main.connect(self.changepassword_MainForm)
                self.close()
            else:
                self.ui.txt_result.setText("Error")
        
#    def changepassword_MainForm(self):
 #           self.main = changepassword_controller()
 #           self.main.show() 
 