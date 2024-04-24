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
        #self.txt_equipo.setText("hola xd")
        self.Cb_Emmanuel.toggled.connect(self.sel_Emmanuel)
        self.Cb_Issac.toggled.connect(self.sel_Issac)

        self.Emmanuel = ""
        self.Issac = ""
    # Área de los Slots
    def sel_Emmanuel(self):
        if self.Cb_Emmanuel.isChecked():
            print("Emmanuel True")
            self.Emmanuel = "EMMANUEL\n"
        else:
            print("Emmanuel False")
            self.Emmanuel = ""
        self.txt_equipo.setPlainText(self.Emmanuel + self.Issac)



    def sel_Issac(self):
        if self.Cb_Issac.isChecked():
            print("Issac True")
            self.Issac = "ISSAC\n"
        else:
            print("Issac False")
            self.Issac = ""
        self.txt_equipo.setPlainText(self.Emmanuel + self.Issac)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
