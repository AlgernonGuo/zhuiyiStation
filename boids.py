from ast import List
import dis
import math
import random
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsScene,
    QGraphicsView,
    QWidget,
)
from PyQt6.QtGui import QPainter, QPen, QColor, QPolygonF
from PyQt6.QtCore import Qt, QTimer, QPointF


class Fish:
    def __init__(self, x, y):
        self.position = QPointF(x, y)
        self.velocity: QPointF = QPointF(
            random.random() * 2 - 1, random.random() * 2 - 1
        )

    def update(self, all_fish: List, window_width, window_height):
        # Update position based on velocity
        self.position += self.velocity
        # 撞墙反弹
        if self.position.x() > window_width:
            self.velocity.setX(-self.velocity.x())
            self.position.setX(window_width)
        elif self.position.x() < 0:
            self.velocity.setX(-self.velocity.x())
            self.position.setX(0)
        if self.position.y() > window_height:
            self.velocity.setY(-self.velocity.y())
            self.position.setY(window_height)
        elif self.position.y() < 0:
            self.velocity.setY(-self.velocity.y())
            self.position.setY(0)

        # 实现boids算法
        # 1. 避免碰撞
        separation_distance: int = 50  # 排斥距离
        max_speed: int = 2  # 最大速度
        for other_fish in all_fish:
            if other_fish == self:
                continue
            distance = math.sqrt(
                (other_fish.position.x() - self.position.x()) ** 2
                + (other_fish.position.y() - self.position.y()) ** 2
            )
            # 仅仅检测前方扇形区域

            if distance < separation_distance:
                self.velocity += (self.position - other_fish.position) / distance
                # 限制速度
                if self.velocity.x() > max_speed:
                    self.velocity.setX(max_speed)
                elif self.velocity.x() < -max_speed:
                    self.velocity.setX(-max_speed)

    def draw(self, painter: QPainter):
        painter.setBrush(Qt.GlobalColor.cyan)
        painter.setPen(QPen(Qt.GlobalColor.cyan))
        painter.save()  # Save current painter state

        painter.translate(self.position)
        angle = math.atan2(self.velocity.y(), self.velocity.x())
        painter.rotate(math.degrees(angle))
        painter.drawPolygon(
            QPolygonF(
                [
                    # QPointF(0, -20),
                    # QPointF(-5, 10),
                    # QPointF(5, 10),
                    QPointF(-10, 5),
                    QPointF(-10, -5),
                    QPointF(10, 0),
                ]
            )
        )
        painter.restore()  # Restore saved state


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Boids Fish Demo")
        self.setGeometry(100, 100, 600, 400)

        self.show()

        self.fish = []
        for i in range(30):
            # fish = Fish(300, 200)
            # 随机位置
            fish = Fish(random.randint(0, 600), random.randint(0, 400))
            self.fish.append(fish)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFish)
        self.timer.start(30)

    def paintEvent(self, event):
        painter = QPainter(self)
        for fish in self.fish:
            fish.draw(painter)

    def updateFish(self):
        window_width = self.width()
        window_height = self.height()
        for fish in self.fish:
            fish.update(self.fish, window_width, window_height)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())
