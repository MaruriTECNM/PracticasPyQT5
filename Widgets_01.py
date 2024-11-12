import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox, #Una caja de confirmacion
    QComboBox, #Una lista de opciones
    QDateEdit, #Para editar la fecha
    QDateTimeEdit, #Para editar la fecha
    QDial, #Dial rotable
    QDoubleSpinBox, #Floats
    QFontComboBox, #Lista de fuentes
    QLabel, #Texto en pantalla, no interactivo
    QLCDNumber, #display de cld
    QLineEdit, #Insertar texto
    QMainWindow, 
    QProgressBar, #Una barra de progresion
    QPushButton, #Un boton
    QRadioButton, #Una lista de objetos de la que solo puedes elegir uno
    QSlider, #Un slider
    QSpinBox, #Un spinner 
    QTimeEdit, #Para editar la hora
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()