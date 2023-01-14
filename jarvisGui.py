
from jarvisUi import Ui_JarvisUi
from PyQt5 import QtCore , QtGui , QtQuickWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import sys
import Jarvis

class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Jarvis.taskexe()


startFunction = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

       super().__init__()

       self.Jarvis_Ui = Ui_JarvisUi()

       self.Jarvis_Ui.setupUi(self)

       self.Jarvis_Ui.pushButton_Start.clicked.connect(self.Startfunc)

       self.Jarvis_Ui.pushButton_Quit.clicked.connect(self.close)
      

    def Startfunc(self):

        self.Jarvis_Ui.movie_1 = QtGui.QMovie("Database/G.U.I material/gui 1 (5).gif")
        self.Jarvis_Ui.Gif_1.setMovie(self.gui.label1)
        self.Jarvis_Ui.movie_1.start()

        self.Jarvis_Ui.movie_2 = QtGui.QMovie("Database/G.U.I material/gui 1 (3).gif")
        self.Jarvis_Ui.Gif_2.setMovie(self.gui.label2)
        self.Jarvis_Ui.movie_2.start()

        self.Jarvis_Ui.movie_3 = QtGui.QMovie("Database/G.U.I material/gui 1 (4).gif")
        self.Jarvis_Ui.Gif_3.setMovie(self.gui.label3)
        self.Jarvis_Ui.movie_3.start()

        self.Jarvis_Ui.movie_4 = QtGui.QMovie("Database/G.U.I material/gui 1 (7).gif")
        self.Jarvis_Ui.Gif_4.setMovie(self.gui.label4)
        self.Jarvis_Ui.movie_4.start()

        self.Jarvis_Ui.movie_5 = QtGui.QMovie("Database/G.U.I material/jarvis 9.webp")
        self.Jarvis_Ui.Gif_5.setMovie(self.gui.label5)
        self.Jarvis_Ui.movie_5.start()

        self.Jarvis_Ui.movie_6 = QtGui.QMovie("Database/G.U.I material/gui 1 (9).gif")
        self.Jarvis_Ui.Gif_6.setMovie(self.gui.label6)
        self.Jarvis_Ui.movie_6.start()

        self.Jarvis_Ui.movie_7 = QtGui.QMovie("Database/G.U.I material/gui 1 (8).gif")
        self.Jarvis_Ui.Gif_7.setMovie(self.gui.label7)
        self.Jarvis_Ui.movie_7.start()

        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunction.start()

def showtime(self):

    current_time = QTime.currentTime()

    label_time = current_time.toString("hh:mm:ss")

    label = "Time :  " + label_time

    self.jarvis_Ui.textbrowser.setText(label)

GuiApp = QApplication(sys.argv)

jarvis_Gui = Gui_Start()

jarvis_Gui.show()

exit(GuiApp.exit_())