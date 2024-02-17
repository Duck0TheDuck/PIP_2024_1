import sys
import numpy as np
import statistics as stat
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_proyecto1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_moda.clicked.connect(self.operacion)
        self.btn_mediana.clicked.connect(self.operacion)
        self.btn_desviacion.clicked.connect(self.operacion)
        self.btn_promedio.clicked.connect(self.operacion)
        self.btn_valormayor.clicked.connect(self.operacion)
        self.btn_valormenor.clicked.connect(self.operacion)
        self.btn_varianza.clicked.connect(self.operacion)

        self.txt_resultado.setEnabled(False)

    # Área de los Slots
    def operacion(self):
        objeto = self.sender()
        nombre = objeto.objectName()

        lista = self.txt_numeros.text()
        lista_float = [float(e) for e in lista.split(" ")]

        if nombre == "btn_moda":
            r = stat.mode(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_mediana":
            r = np.median(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_desviacion":
            r = np.std(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_promedio":
            r = np.average(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_valormayor":
            r = np.max(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_valormenor":
            r = np.min(lista_float)
            self.txt_resultado.setText(str(r))
        elif nombre == "btn_varianza":
            r = np.var(lista_float)
            self.txt_resultado.setText(str(r))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
