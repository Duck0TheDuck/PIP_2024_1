import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_00_Plantilla.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_emma.click.connect(self.clic_emma)
        self.rb_emma.toggled.connect(self.toggled_emma)

    # Área de los Slots
    def clic_emma(self):
        print("Hiciste clic")

    def toggeld_emma(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

