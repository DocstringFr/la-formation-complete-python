from PySide2 import QtWidgets, QtGui, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()

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
  
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()