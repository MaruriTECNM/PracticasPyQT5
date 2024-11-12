#Ejemplo de aplicacion simple que reune lo aprendido hasta ahora.
#El usuario introduce dos numeros en dos qlabels, posteriormente presiona un boton y se hacen las operaciones básicas.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora simple")
        self.setFixedSize(QSize(800,600))
        self.Textos()
        self.Boton()

        layout = QVBoxLayout()#Layout y agregar widgets a la ventana
        layout.addWidget(self.Numero1)
        layout.addWidget(self.Numero2)
        layout.addWidget(self.BotonSuma)
        layout.addWidget(self.BotonResta)
        layout.addWidget(self.BotonMultiplicacion)
        layout.addWidget(self.Resultado)
        
        widget = QWidget()#Creacion del widget principal
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        #Lista de eventos
        self.BotonSuma.clicked.connect(self.eventoSuma)#Suma
        self.BotonResta.clicked.connect(self.eventoSubstracion)#Resta
        self.BotonMultiplicacion.clicked.connect(self.eventoMultiplicacion)#Multiplicacion
    
    def Textos(self):
        self.Numero1 = QLineEdit("0")#Creacion de una entrada de texto, valor inicial de 0.
        self.Numero1.setFixedSize(QSize(100,25))

        self.Numero2 = QLineEdit("0")#Creacion de una entrada de texto, valor inicial de 0.
        self.Numero2.setFixedSize(QSize(100,25))

        self.Resultado = QLabel("Resultado: ")
    
    def Boton(self):#Creacion de los botones a usar
        self.BotonSuma = QPushButton("Sumar numeros")#Boton de suma
        self.BotonSuma.setFixedSize(QSize(100,40))

        self.BotonMultiplicacion = QPushButton("Multiplicar numeros")#Boton de multiplicacion
        self.BotonMultiplicacion.setFixedSize(QSize(100,40))

        self.BotonResta = QPushButton("Restar numeros")#Boton de resta
        self.BotonResta.setFixedSize(QSize(100,40))
    
    def eventoSuma(self):#Evento de suma
        Numero1 = int(self.Numero1.text())#Se guarda en la variable "Numero1" el valor casteado a int del texto del widget Numero1
        Numero2 = int(self.Numero2.text())
        Sumatoria=Numero1+Numero2#Se realiza la suma
        self.Resultado.setText("Resultado: {}".format(Sumatoria))#Se imprime en pantalla usando .format.
    
    def eventoSubstracion(self):
        Numero1 = int(self.Numero1.text())
        Numero2 = int(self.Numero2.text())
        Substraccion=Numero1-Numero2
        self.Resultado.setText("Resultado: {}".format(Substraccion))
    
    def eventoMultiplicacion(self):
        Numero1 = int(self.Numero1.text())
        Numero2 = int(self.Numero2.text())
        Producto=Numero1*Numero2
        self.Resultado.setText("Resultado: {}".format(Producto))

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()