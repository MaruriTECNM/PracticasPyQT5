#Creación de un menú contextual dentro de la ventana de trabajo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("Opcion 1", self))
        context.addAction(QAction("Opcion 2", self))
        context.addAction(QAction("Opcion 3", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()