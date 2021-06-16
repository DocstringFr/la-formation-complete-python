from PySide2 import QtWidgets, QtGui, QtCore
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_default_values()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.le_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.le_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverser devises")

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.le_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.le_montantConverti)
        self.layout.addWidget(self.btn_inverser)
    
    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesFrom.setCurrentText("EUR")
        self.cbb_devisesTo.setCurrentText("EUR")
        self.le_montant.setValue(100)
        self.le_montantConverti.setValue(100)
        self.le_montant.setRange(1, 1000000)
        self.le_montantConverti.setRange(1, 1000000)

 
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()