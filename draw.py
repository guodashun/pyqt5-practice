import sys
from PyQt5.QtCore import Qt, QLineF, QPoint, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QPen, QPainterPath, QFont
import os
import math

pic_dir = "/home/zjunlict-vision-1/luckky/train_set/"
pics = [pic_dir + i for i in sorted(os.listdir(pic_dir))]


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.drawingPath = None
        self.start = QPoint(0, 0)
        self.end = QPoint(0, 0)
        self.angle = 0.0
        self.index = 0
        self.image = QPixmap(pics[self.index])
        self.resize(self.image.width() * 10, self.image.height() * 10)
        print(pics[self.index])
        next_button = QPushButton("Next", self)
        back_button = QPushButton("Back", self)
        next_button.move(100, 10)
        back_button.move(0, 10)
        next_button.clicked.connect(self.next_pic)
        back_button.clicked.connect(self.back_pic)
        self.show()

    def next_pic(self):
        if self.index >= len(pics):
            self.index = 0
        else:
            self.index += 1
        self.image = QPixmap(pics[self.index])
        print(pics[self.index])
        self.update()

    def back_pic(self):
        self.index -= 1
        self.image = QPixmap(pics[self.index])
        print(pics[self.index])
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        painter.drawLine(self.start, self.end)
        font = QFont()
        font.setPixelSize(50)
        painter.setFont(font)
        painter.drawText(self.end, str(self.angle / 180 * math.pi))

    def mousePressEvent(self, event):
        self.start = event.pos()
        self.end = event.pos()
        # if event.button() == Qt.LeftButton:
        # # start a new QPainterPath and *move* to the current point
        # self.drawingPath = QPainterPath()
        # self.drawingPath.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.angle = QLineF(self.start, self.end).angle()
        if event.buttons() and Qt.LeftButton:
            # add a line to the painter path, without "removing" the pen
            # self.drawingPath.lineTo(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        pass
        # if event.button() == Qt.LeftButton and self.drawingPath:
        #     # draw the painter path to the pixmap
        #     painter = QPainter(self.image)
        #     painter.setPen(QPen(QColor(121,252,50,50), 20, Qt.SolidLine))
        #     painter.drawPath(self.drawingPath)
        #     self.drawingPath = None
        #     self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    sys.exit(app.exec_())
