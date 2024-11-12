#Ejemplo de creación de multiples eventos y paso de variables.
#En este ejemplo se crearons dos botones, al presionarse un botón este de deshabilita pero habilita al otro botón.
#Al mismo tiempo cada vez que se presiona un botón el título de la ventana cambia.
#Cuando el título de la ventana cambie a "No deberias ver esto", ambos botones quedan deshabilitados.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from random import choice

titulos = [#Creación de lista de títulos a elegir
    'Ventana', 
    'Me llamo Ralph', 
    'Me mordi la lengua escribiendo este codigo', 
    'Hace calor', 
    'Holaaaaaa', 
    'No deberias ver esto'
    ]#Lista de posibles titulos de ventana


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cambiar la interfaz")
        self.setFixedSize(QSize(800,600))
        self.primerboton()#Llama al boton
        self.segundoboton()#Llama al segundo boton
        self.windowTitleChanged.connect(self.cambiarTitulo)#El vigilante del evento, solo se activa cuando el titulo cambia a uno diferente del anterior

    def primerboton(self):
        self.boton1 = QPushButton("Presioname", self)#Se le asigna el a la variable global self.boton1, esto se hace dado que esta variable es llamada en otros lugares.
        self.boton1.setFixedSize(QSize(150,50))#Cambiar de tamaño del botón.
        self.boton1.move(350,250)#Posición absoluta del botón
        self.boton1.clicked.connect(self.evento)#Evento, cuando se le hace click un evento es llamado.
    
    def segundoboton(self):
        self.boton2 = QPushButton("No me presiones!", self)
        self.boton2.setFixedSize(QSize(150,50))
        self.boton2.move(350,300)
        self.boton2.setEnabled(False)
        self.boton2.clicked.connect(self.evento2)#Evento no.2
    
    def evento(self):#Evento
        self.boton1.setText("Deja de presionarme!")#Cambia el texto del primer boton
        self.boton2.setText("Presioname a mi, a mi!")#Cambia el texto del segundo boton
        self.boton1.setEnabled(False)#Deshabilitar el primer boton
        self.boton2.setEnabled(True)#Habilitar el segundo boton
        self.nuevoTitulo = choice(titulos)#Guarda en la variable "nuevoTitulo" el nuevo titulo de la ventana, se utiliza el "self." como prefijo dado su uso global.
        self.setWindowTitle(self.nuevoTitulo)#Cambia el titulo de la ventana de acuerdo a la variable "nuevoTitulo".
    
    def evento2(self):#Evento num 2, hace lo inverso que el evento de arriba.
        self.boton1.setText("Presioname!")
        self.boton2.setText("Deja de presionarme!")
        self.boton1.setEnabled(True)
        self.boton2.setEnabled(False)
        self.nuevoTitulo = choice(titulos)
        self.setWindowTitle(self.nuevoTitulo)
    
    def cambiarTitulo(self, titulos):#El evento que vigila el cambio de titulos, tiene como entrada la variable global "titulos".
        if titulos == 'No deberias ver esto':#Si por azar se seleciona ese titulo
            self.boton1.setEnabled(False)#Ambos botones se deshabilitan
            self.boton2.setEnabled(False)
        
app = QApplication(sys.argv)
window = Ventana()
window.show()
app.exec()