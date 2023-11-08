import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget

from Ui_K8s import Ui_K8s


class K8sInterface(QWidget, Ui_K8s):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
