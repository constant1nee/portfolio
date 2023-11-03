from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtGui

class SimpleInterestWindow(QMainWindow):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant')

        self.label = QLabel(self)
        self.label.setText('Вставьте латинскую букву "x", если хотите найти этот параметр!')
        self.label.move(100, 125)
        self.label.resize(450, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: #aebccf')

        self.label_1 = QLabel(self)
        self.label_1.setText('PV = настоящий капитал; n = длительность; FV = будущий капитал')
        self.label_1.move(95, 150)
        self.label_1.resize(455, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet('background-color: #aebccf')


        self.label_pv = QLabel(self)
        self.label_pv.setText('PV')
        self.label_pv.move(140, 205)
        self.label_pv.resize(20, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_pv.setFont(font)
        self.label_pv.setStyleSheet('background-color: #aebccf')

        self.label_pr = QLabel(self)
        self.label_pr.setText('%')
        self.label_pr.move(140, 255)
        self.label_pr.resize(20, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_pr.setFont(font)
        self.label_pr.setStyleSheet('background-color: #aebccf')

        self.label_n = QLabel(self)
        self.label_n.setText('n')
        self.label_n.move(140, 305)
        self.label_n.resize(10, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_n.setFont(font)
        self.label_n.setStyleSheet('background-color: #aebccf')

        self.label_fv = QLabel(self)
        self.label_fv.setText('FV')
        self.label_fv.move(140, 355)
        self.label_fv.resize(20, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_fv.setFont(font)
        self.label_fv.setStyleSheet('background-color: #aebccf')

        self.back_button = QPushButton(self)
        self.back_button.move(500, 525)
        self.back_button.resize(55, 25)
        self.back_button.setText('Назад')
        self.back_button.clicked.connect(self.get_back)
        self.back_button.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "\n"                    
                                      "QPushButton::hover{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #0b3a73;\n"
                                      "    border: 2px solid #aebccf;\n"
                                      "    color: #aebccf;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input = QLineEdit(self)
        self.parameter_input.move(200, 200)
        self.parameter_input.resize(275, 25)
        self.parameter_input.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")
        self.parameter_input_2 = QLineEdit(self)
        self.parameter_input_2.move(200, 250)
        self.parameter_input_2.resize(275, 25)
        self.parameter_input_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_3 = QLineEdit(self)
        self.parameter_input_3.move(200, 300)
        self.parameter_input_3.resize(275, 25)
        self.parameter_input_3.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_4 = QLineEdit(self)
        self.parameter_input_4.move(200, 350)
        self.parameter_input_4.resize(275, 25)
        self.parameter_input_4.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.calc_button = QPushButton(self)
        self.calc_button.move(250, 400)
        self.calc_button.resize(100, 25)
        self.calc_button.setText('Расчитать')
        self.calc_button.clicked.connect(self.calculate_simp)
        self.calc_button.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "\n"                    
                                      "QPushButton::hover{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #0b3a73;\n"
                                      "    border: 2px solid #aebccf;\n"
                                      "    color: #aebccf;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

    def calculate_simp(self):
        pv_value = self.parameter_input.text()
        pr_value = self.parameter_input_2.text()
        n_value = self.parameter_input_3.text()
        fv_value = self.parameter_input_4.text()
        if fv_value == 'x':
             expression = int(pv_value) + ((int(pv_value) * (float(pr_value) / 100)) * int(n_value))
             self.parameter_input_4.setText(str(expression))
        elif pv_value == 'x':
             expression = int(fv_value) / ((float(pr_value) / 100) * int(n_value) + 1)
             self.parameter_input.setText(str(expression))
        elif pr_value == 'x':
             expression = (int(pv_value) - int(fv_value)) / -(int(pv_value) / (100 / int(n_value)))
             self.parameter_input_2.setText(str(expression))
        elif n_value == 'x':
             expression = (int(pv_value) - int(fv_value)) / -(int(pv_value) * (float(pr_value) / 100))
             self.parameter_input_3.setText(str(expression))

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def get_back(self):
        self.dialog.show()
        self.close()
