import cv2
import opencv_engine
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
import sys
sys.path.append("..")


class System_controller(object):
    def __init__(self, video_path, ui):
        self.video_path = video_path
        self.ui = ui
        self.init_video_info()
        self.set_video_player()

    def init_video_info(self):
        videoinfo = opencv_engine.opencv_engine.getvideoinfo(
            self.video_path)
        self.vc = videoinfo["vc"]
        self.video_fps = videoinfo["fps"]
        self.video_total_frame_count = videoinfo["frame_count"]
        self.video_width = videoinfo["width"]
        self.video_height = videoinfo["height"]

    def processVideoFile(self):
        opencv_engine.opencv_engine.writevideofile("")
