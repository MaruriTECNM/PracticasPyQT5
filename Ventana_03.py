#Ejemplo de creación de eventos.
#En este ejemplo se crea una ventana con un botón que imprime un texto en la consola.
#El primer evento solo manda un sencillo "hola mundo".
#Mientras que el segundo evento verifica si el botón fue presionado ("checked")

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boton que hace algo")
        self.setFixedSize(QSize(800,600))
        self.botones()

    def botones(self):
        button = QPushButton("Boton", self)#Creacion del boton
        button.setFixedSize(QSize(100,50))#Dimensiones del boton
        button.move(350,250)#Posicion absoluta
        button.setCheckable(True)#Por default los botones no estan "checkeados", así que se se habilita la funcion de ser checkeados
        button.clicked.connect(self.evento)#Llamado de evento
        button.clicked.connect(self.evento2)#Llamado de evento
    
    def evento(self):
        print("Hola mundo!")#Imprime un texto en la consola.
    
    def evento2(self, checked):#Paso de variables
        self.evento2 = checked#Se le asigna el estado de "checked" al boton
        print(self.evento2)

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()