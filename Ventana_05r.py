#Ejemplo de conexión de dos Widgets PyQT5.
#En este ejemplo se crearan dos widgets, uno de tipo input que lee lo que usuario introduce.
#Y el segundo que escribe en pantalla lo mismo que escribió el usuario.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conexión de dos widgets PyQT5")
        self.setFixedSize(QSize(800,600))
        self.WidgetsUI()#Se llama la funcion WidgetsUI para poder usar los widgets.
        
        interfaz = QVBoxLayout()#Creación de layout
        interfaz.addWidget(self.texto)#Añadimos ambos widgets
        interfaz.addWidget(self.lectura)

        cont = QWidget()#Creacion del widget principal
        cont.setLayout(interfaz)
        self.setCentralWidget(cont)

    def WidgetsUI(self):
        self.texto = QLabel()#Se crea un QLabel() que es un texto en pantalla.
        self.lectura = QLineEdit()#Se crea un QLineEdit() que sirve a modo de input().
        self.lectura.textChanged.connect(self.texto.setText)#Cuando el texto del cambio "Lectura" cambie, el valor de texto también lo hara.

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()