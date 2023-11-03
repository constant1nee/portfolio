from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtGui
from s_int_window import SimpleInterestWindow
from c_int_window import CompoundedInterestWindow
from cont_int_window import ContInterestWindow


class MenuWindow(QMainWindow):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Если вам необходимо расчитать процентную ставку,')
        self.label.move(120, 125)
        self.label.resize(380, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: #aebccf')

        self.label_2 = QLabel(self)
        self.label_2.setText('длительность или будущий капитал, то нажмите "Простые проценты"')
        self.label_2.move(80, 150)
        self.label_2.resize(475, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: #aebccf')

        self.label_3 = QLabel(self)
        self.label_3.setText('Если вам необходимо расчитать более сложные параметры такие как,')
        self.label_3.move(75, 175)
        self.label_3.resize(490, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('background-color: #aebccf')

        self.label_4 = QLabel(self)
        self.label_4.setText('кол-во начислений в год, кол-во платежей в год, то нажмите')
        self.label_4.move(90, 200)
        self.label_4.resize(430, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet('background-color: #aebccf')

        self.label_5 = QLabel(self)
        self.label_5.setText('"Сложные проценты"')
        self.label_5.move(245, 225)
        self.label_5.resize(150, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet('background-color: #aebccf')

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant')

        self.button_1 = QPushButton(self)
        self.button_1.move(150, 300)
        self.button_1.resize(150, 50)
        self.button_1.setText('Простые проценты')
        self.button_1.clicked.connect(self.open_simp_interest_window)
        self.button_1.setStyleSheet("QPushButton{\n"
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

        self.button_2 = QPushButton(self)
        self.button_2.move(325, 300)
        self.button_2.resize(150, 50)
        self.button_2.setText('Сложные проценты')
        self.button_2.clicked.connect(self.open_comp_interest_window)
        self.button_2.setStyleSheet("QPushButton{\n"
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

        self.button_3 = QPushButton(self)
        self.button_3.move(235, 375)
        self.button_3.resize(150, 50)
        self.button_3.setText('Непрерывные проценты')
        self.button_3.clicked.connect(self.open_cont_interest_window)
        self.button_3.setStyleSheet("QPushButton{\n"
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

    def open_simp_interest_window(self):
        self.dialog = SimpleInterestWindow(self)
        self.dialog.show()
        self.hide()

    def open_comp_interest_window(self):
        self.dialog = CompoundedInterestWindow(self)
        self.dialog.show()
        self.hide()

    def open_cont_interest_window(self):
        self.dialog = ContInterestWindow(self)
        self.dialog.show()
        self.hide()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def get_back(self):
        self.dialog.show()
        self.close()