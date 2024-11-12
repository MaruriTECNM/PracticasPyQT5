from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()