import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pac-Man LTKK")
        self.setGeometry(300, 300, 500, 500)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.blue)
        self.setPalette(p)


    def buttons(self, QMainWindow):

        button_new_game = QPushButton('New game', self)
        button_new_game.move(200, 100)

        button_about = QPushButton('About', self)
        button_about.move(200, 200)

        button_exit = QPushButton('Exit', self)
        button_exit.move(200, 300)

        self.show()

    def image_background(self, QMainWindow):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('pacman.png'))
        self.move(150, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.buttons(MainWindow)
    window.image_background(MainWindow)

    window.show()

    sys.exit(app.exec_())
