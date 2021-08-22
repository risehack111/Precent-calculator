import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


#Code

def res():
    chislo = float(ui.lineEdit.text())
    precent = int(ui.lineEdit_2.text())
    result = (chislo * precent) / 100
    result = round(result, 3)
    ui.lineEdit_3.setText(str(result))






ui.pushButton.clicked.connect(res)

sys.exit(app.exec_())