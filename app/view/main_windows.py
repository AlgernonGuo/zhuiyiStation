from PyQt6.QtWidgets import QPushButton, QApplication
from qfluentwidgets import SplashScreen, FluentWindow, Dialog, PushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap
from qfluentwidgets import FluentIcon as FIF

from app.view.home_interface import HomeInterface


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.addSubInterface(HomeInterface(self), FIF.HOME, self.tr('Home'))
        self.splashScreen.finish()

    def initWindow(self):
        self.setWindowTitle("Fluent Widgets")
        icon = QIcon(QPixmap("./app/resource/zhuiyi.png").scaled(318, 106))
        self.setWindowIcon(icon)
        self.resize(960, 780)
        self.setMinimumWidth(760)

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        qbtn = PushButton("Quit", self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 150)

        btn = PushButton("Click Me", self)
        btn.move(100, 100)

        self.center()
        self.show()

    def closeEvent(self, event):
        w = Dialog("提示🔔", "Are you sure to quit?", self)
        if w.exec():
            print("Yes button is pressed")
            event.accept()
        else:
            print("Cancel button is pressed")
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Service:
    i = 1

    def __init__(self):
        self.i = 1

    def add():
        Service.i += 1
        print(Service.i)
