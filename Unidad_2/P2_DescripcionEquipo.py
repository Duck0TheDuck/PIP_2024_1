import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signal
        self.datos_intregante ={
            1:["Emmanuel","Dormir",20,"0+",":/Meme/Em.jpg"],
            2:["Isaac", "Jugar y chamba", 20, "0-",":/Meme/Issac.jpg"],
        }

        self.btn_atras.cliked.connect(self.atras)
        self.btn_adelante.cliked.connect(self.adelante)

        self.index_control = -1


    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
        self.index_control -= 1
        datos = self.datos_intregante(self.index_control)
        print(datos)
        self.btn_adelante.setEnabled(True)


    def adelante(self):

        self.index_control += 1
        datos = self.datos_intregante(self.index_control)
        print(datos)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
