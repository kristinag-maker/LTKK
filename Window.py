import sys

from PyQt5 import QtMultimedia
from PyQt5.QtCore import Qt, QSize, QUrl, QDir, QCoreApplication
from PyQt5.QtGui import  QImage, QPalette, QBrush
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pac-Man LTKK")
        self.setGeometry(300, 300, 500, 500)



    def buttons(self, QMainWindow):
        button_new_game = QPushButton('New game', self)
        button_new_game.move(200, 240)

        button_about = QPushButton('About', self)
        button_about.move(10, 10)

        button_exit = QPushButton('Exit', self)
        button_exit.move(400, 10)
        button_exit.clicked.connect(self.izadji)

        self.show()

    def izadji(self):
        self.close()

    def image_background(self, QMainWindow):
        oImage = QImage("pacman.png")
        sImage = oImage.scaled(QSize(450, 500))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.label = QLabel('Test', self)  # test, if it's really backgroundimage
        self.label.setGeometry(50, 50, 200, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.buttons(MainWindow)
    window.image_background(MainWindow)
    window.show()

    sys.exit(app.exec_())
