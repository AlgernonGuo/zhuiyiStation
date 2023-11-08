from PyQt6.QtWidgets import QPushButton, QApplication
from qfluentwidgets import SplashScreen, FluentWindow, Dialog, PushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap
from qfluentwidgets import FluentIcon as FIF
from app.view.home_interface import HomeInterface
from app.view.k8s_interface import K8sInterface


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()
        self.addSubInterface(HomeInterface(self), FIF.HOME, self.tr("Home"))
        self.addSubInterface(K8sInterface(self), FIF.IOT, self.tr("K8s"))
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
