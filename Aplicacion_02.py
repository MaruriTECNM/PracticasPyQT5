#Aplicacion que muestra una palabra aleatoria de una lista de palabras.
#Además posee un botón que cambia la palabra mostrada.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from random import randint
import sys

palabras = [#Lista de palabras
    "Honkai",
    "Star",
    "Rail",
    "Stelle",
    "Caelus",
    "Xueyi",
    "Hanya"
]

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wordle test")
        self.texto()
        self.botonera()

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.textPartido)
        layout.addWidget(self.Boton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def texto(self):
        Palabra = palabras[randint(0,len(palabras)-1)]
        self.arrayPalabra = [*Palabra]
        self.text = QLabel("Chosen word: {}".format(Palabra))
        self.textPartido = QLabel("Split in characters: {}".format(self.arrayPalabra))
    
    def botonera(self):
        self.Boton = QPushButton("Press to reroll")
        self.Boton.setFixedSize(QSize(200,40))
        self.Boton.move(300,400)
        self.Boton.clicked.connect(self.reroll)
    
    def reroll(self):
        Palabra = palabras[randint(0,len(palabras)-1)]
        self.arrayPalabra = [*Palabra]
        self.text.setText("Chosen word: {}".format(Palabra))
        self.textPartido.setText("Split in characters: {}".format(self.arrayPalabra))

app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()