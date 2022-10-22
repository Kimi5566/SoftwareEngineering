from UI_main import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QDialog, QLabel
from video_controller import *
import sys
sys.path.append("..")


class Main_controller(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btn_openFile.clicked.connect(self.open_file)

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open file Window", "./", "Video Files(*.mp4 *.avi)")
        self.video_path = filename
        self.video_controller = Video_controller(video_path=self.video_path,
                                                 ui=self.ui)

        self.ui.btn_play.clicked.connect(self.video_controller.play)
        self.ui.btn_stop.clicked.connect(self.video_controller.stop)
        self.ui.btn_pause.clicked.connect(self.video_controller.pause)
