import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QPoint


class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.last_point = QPoint()
        self.current_point = QPoint()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mouse Drawing")
        self.setGeometry(100, 100, 800, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(QColor("black"))
        painter.setPen(pen)
        painter.drawLine(self.last_point, self.current_point)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_point = event.pos()
            self.current_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton:
            self.last_point = self.current_point
            self.current_point = event.pos()
            self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = DrawingWidget()
        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
