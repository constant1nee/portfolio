from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtGui
import sympy as sym

class CompoundedInterestWindow(QMainWindow):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant')

        self.label = QLabel(self)
        self.label.setText('Вставьте латинскую букву "x", если хотите найти этот параметр!')
        self.label.move(80, 50)
        self.label.resize(450, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: #aebccf')

        self.label_2 = QLabel(self)
        self.label_2.setText('PV = настоящий капитал; n = длительность; FV = будущий капитал;')
        self.label_2.move(75, 75)
        self.label_2.resize(465, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: #aebccf')

        self.label_3 = QLabel(self)
        self.label_3.setText('PMT = кол-во зачислений в мес.; C/Y = частота; P/Y = частота')
        self.label_3.move(80, 100)
        self.label_3.resize(435, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('background-color: #aebccf')

        self.label_pv = QLabel(self)
        self.label_pv.setText('PV')
        self.label_pv.move(140, 155)
        self.label_pv.resize(20, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_pv.setFont(font)
        self.label_pv.setStyleSheet('background-color: #aebccf')

        self.label_pr = QLabel(self)
        self.label_pr.setText('%')
        self.label_pr.move(140, 205)
        self.label_pr.resize(20, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_pr.setFont(font)
        self.label_pr.setStyleSheet('background-color: #aebccf')

        self.label_n = QLabel(self)
        self.label_n.setText('n')
        self.label_n.move(140, 255)
        self.label_n.resize(10, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_n.setFont(font)
        self.label_n.setStyleSheet('background-color: #aebccf')

        self.label_pmt = QLabel(self)
        self.label_pmt.setText('PMT')
        self.label_pmt.move(140, 305)
        self.label_pmt.resize(30, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_pmt.setFont(font)
        self.label_pmt.setStyleSheet('background-color: #aebccf')

        self.label_py = QLabel(self)
        self.label_py.setText('P/Y')
        self.label_py.move(140, 355)
        self.label_py.resize(30, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_py.setFont(font)
        self.label_py.setStyleSheet('background-color: #aebccf')

        self.label_cy = QLabel(self)
        self.label_cy.setText('C/Y')
        self.label_cy.move(140, 405)
        self.label_cy.resize(30, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_cy.setFont(font)
        self.label_cy.setStyleSheet('background-color: #aebccf')

        self.label_fv = QLabel(self)
        self.label_fv.setText('FV')
        self.label_fv.move(140, 455)
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
        self.parameter_input.move(200, 150)
        self.parameter_input.resize(275, 25)
        self.parameter_input.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_2 = QLineEdit(self)
        self.parameter_input_2.move(200, 200)
        self.parameter_input_2.resize(275, 25)
        self.parameter_input_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_3 = QLineEdit(self)
        self.parameter_input_3.move(200, 250)
        self.parameter_input_3.resize(275, 25)
        self.parameter_input_3.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_4 = QLineEdit(self)
        self.parameter_input_4.move(200, 300)
        self.parameter_input_4.resize(275, 25)
        self.parameter_input_4.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_5 = QLineEdit(self)
        self.parameter_input_5.move(200, 350)
        self.parameter_input_5.resize(275, 25)
        self.parameter_input_5.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_6 = QLineEdit(self)
        self.parameter_input_6.move(200, 400)
        self.parameter_input_6.resize(275, 25)
        self.parameter_input_6.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.parameter_input_7 = QLineEdit(self)
        self.parameter_input_7.move(200, 450)
        self.parameter_input_7.resize(275, 25)
        self.parameter_input_7.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.calc_button = QPushButton(self)
        self.calc_button.move(250, 525)
        self.calc_button.resize(100, 25)
        self.calc_button.setText('Расчитать')
        self.calc_button.clicked.connect(self.calculate_comp)
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

    def calculate_comp(self):
        pv_value = self.parameter_input.text()
        pr_value = self.parameter_input_2.text()
        n_value = self.parameter_input_3.text()
        pmt_value = self.parameter_input_4.text()
        cy_value = self.parameter_input_5.text()
        py_value = self.parameter_input_6.text()
        fv_value = self.parameter_input_7.text()
        if fv_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((int(pv_value) * ((1 + ((float(pr_value) / 100) / int(cy_value))) **
                                                      (int(n_value) * int(py_value))) - x), x)
            self.parameter_input_7.setText(str(solution)[1:-1])
        elif pv_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((x * ((1 + ((float(pr_value) / 100) / int(cy_value))) **
                                        (int(n_value) * int(py_value))) - int(fv_value)), x)
            self.parameter_input.setText(str(solution)[1:-1])
        elif n_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((int(pv_value) * ((1 + ((float(pr_value) / 100) / int(cy_value))) **
                                        (x * int(py_value))) - float(fv_value)), x)
            self.parameter_input_3.setText(str(solution)[1:-1])
        elif pr_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((int(pv_value) * ((1 + ((x / 100) / int(cy_value))) **
                                        (int(n_value) * int(py_value))) - float(fv_value)), x)
            self.parameter_input_2.setText(str(solution)[1:-1])
        elif cy_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((int(pv_value) * ((1 + ((float(pr_value) / 100) / x)) **
                                        (int(n_value) * int(py_value))) - float(fv_value)), x)
            self.parameter_input_5.setText(str(solution)[1:-1])
        elif py_value == 'x' and pmt_value == '0':
            x = sym.Symbol('x')
            solution = sym.solveset((int(pv_value) * ((1 + ((float(pr_value) / 100) / int(cy_value))) **
                                        (int(n_value) * x)) - float(fv_value)), x)
            self.parameter_input_6.setText(str(solution)[1:-1])

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def get_back(self):
        self.dialog.show()
        self.close()