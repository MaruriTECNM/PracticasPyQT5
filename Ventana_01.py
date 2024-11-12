#Ejemplo de creacion de ventana básica.
#En este código solo se crea una ventana básica que contiene un botón.

from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import QSize
import sys

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana") #Titulo de la aplicacion
        self.setFixedSize(QSize(800,600)) #Tamaño fijo de la ventana
        button = QPushButton("Presioname!") #Boton que dice presioname
        button.setFixedSize(QSize(200,200))#Modificar el tamaño del boton
        button.move(500,500)
        self.setCentralWidget(button)#Se usa para colocar el boton en la pantalla

app = QApplication(sys.argv)#Creacion de la aplicacion, se usa sys.argv para pasar los argumentos a la aplicacion
window = Principal()
window.show()
app.exec()#Ejecutar el ciclo de la aplicacion