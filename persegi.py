import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from decimal import Decimal

qtcreator_file2  = "persegi.ui" # Enter file here.
Ui_PersegiWindow, QtBaseClass = uic.loadUiType(qtcreator_file2)


# Class Window Persegi
class MyPersegiWindow(QtWidgets.QMainWindow, Ui_PersegiWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_PersegiWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal) # Windows as Modal
        self.setupUi(self)
        self.btnHitung.clicked.connect(self.hitung)

    def hitung(self):
        panjang = Decimal(self.txtPanjang.text())
        lebar = Decimal(self.txtLebar.text())
        luas = panjang * lebar
        keliling = (2 * panjang) + (2 * lebar)
        self.txtLuas.setText(str(luas))
        self.txtKeliling.setText(str(keliling))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    persegi = MyPersegiWindow()
    persegi.show() 
    sys.exit(app.exec_())