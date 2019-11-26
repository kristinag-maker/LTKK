import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Hello World")
        self.setGeometry(200, 200, 200, 200)

        label = QLabel("This is so cool!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
