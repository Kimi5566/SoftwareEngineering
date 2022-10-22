from PyQt5.QtWidgets import QApplication

from login_controller import Login_controller


import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login_controller()
    login.show()

    sys.exit(app.exec_())


"""
import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()

"""
