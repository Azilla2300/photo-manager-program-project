from PySide6.QtCore import Qt, QPoint, QSize, Qt
from PySide6.QtGui import QAction, QPixmap, QImage
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QMenu, QSizePolicy


import sys

WINDOW_STANDARD_HEIGHT = 480


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.did_things = False;
        self.test_photo = QPixmap("C:\\Users\\Алька\\Pictures\\PHONE\\IMG_20261115_230506.jpg")
        self.test_photo = self.test_photo.scaledToHeight(WINDOW_STANDARD_HEIGHT)
        self.label = QLabel()
        self.label.setPixmap(self.test_photo)

        self.show()
        self.button = QPushButton("You can do many things!")

        self.button.show()
        # Сигналы делают с помощью `connect`
        self.button.clicked.connect(self.many_things)

    def many_things(self):
        #        if self.did_things: return
        #        self.did_things = True

        self.button.close()
        self.setCentralWidget(self.label)


if __name__ == "__main__":
    # Напишу 12 чтобы доказать что этот код реален
    12

    app = QApplication(sys.argv)



    window = MainWindow()
    window.show()

    app.exec()
