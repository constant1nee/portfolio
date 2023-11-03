from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter
from sign_in_window import SignInWindow
from sign_up_window import SignUpWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Financial Assistant')
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.move(195, 125)
        self.label.resize(210, 25)
        self.label.setStyleSheet('background-color: #aebccf')
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant')

        self.button_1 = QPushButton(self)
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
        self.button_1.move(225, 200)
        self.button_1.resize(150, 50)
        self.button_1.setText('Войти')
        self.button_1.clicked.connect(self.open_sign_up_window)

        self.button_2 = QPushButton(self)
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
        self.button_2.move(225, 275)
        self.button_2.resize(150, 50)
        self.button_2.setText('Зарегистрироваться')
        self.button_2.clicked.connect(self.open_sign_in_window)

        self.button_3 = QPushButton(self)
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
        self.button_3.move(225, 350)
        self.button_3.resize(150, 50)
        self.button_3.setText('О нас')

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def open_sign_in_window(self):
        self.dialog = SignInWindow(self)
        self.dialog.show()
        self.hide()

    def open_sign_up_window(self):
        self.dialog = SignUpWindow(self)
        self.dialog.show()
        self.hide()
