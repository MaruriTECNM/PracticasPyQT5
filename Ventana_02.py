#Ejemplo de creacion de ventana con botones.
#En este código se crea una ventana con un botón y un texto en pantalla.
#Con este código se aprendió como separar los elementos de una ventana en diferentes definiciones.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()#La ventana solo ejecuta el tamaño y llama a la funcion de elementos
        self.setWindowTitle("Ejemplo de ventana 800 por 600")
        self.setFixedSize(QSize(800,600))
        self.elementos()
        self.texto()

    def elementos(self):#Se separan los elementos de la interfaz en una deficion aparte
        button = QPushButton("Boton!", self)
        button.setFixedSize(QSize(100,50))
        button.move(300,300)
    
    def texto(self):#Se separan los elementos de forma individual
        label = QLabel("Hola mundo!", self)
        label.move(320,360)

App = QApplication(sys.argv)
window = ventana()
window.show()
App.exec()