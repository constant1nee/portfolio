import sys
from PyQt5.QtWidgets import QApplication, QDialog
from main_window import MainWindow


app = QApplication(sys.argv)
dialog = QDialog()
ex = MainWindow()
ex.show()


sys.exit(app.exec_())