from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtGui
from random import shuffle
import sqlite3

db = sqlite3.connect('fin_assist.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS info(login TEXT, password TEXT)''')
db.commit()

class SignInWindow(QMainWindow):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Регистрация')
        self.label.move(265, 100)
        self.label.resize(85, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: #aebccf')

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant (Регистрация)')

        self.label_1 = QLabel(self)
        self.label_1.move(105, 170)
        self.label_1.resize(50, 15)
        self.label_1.setText('Логин:')
        font = QtGui.QFont()
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet('background-color: #aebccf')

        self.label_2 = QLabel(self)
        self.label_2.move(105, 220)
        self.label_2.resize(60, 15)
        self.label_2.setText('Пароль:')
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: #aebccf')


        self.label_3 = QLabel(self)
        self.label_3.move(90, 330)
        self.label_3.resize(425, 15)
        self.label_3.setText('Требования к созданию пароля: длинна не менее 8 символов')
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('background-color: #aebccf')

        self.status = QLabel(self)
        self.status.move(100, 200)
        self.status.resize(500, 400)

        self.password_input = QLineEdit(self)
        self.password_input.move(175, 165)
        self.password_input.resize(275, 25)
        self.password_input.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.password_input_2 = QLineEdit(self)
        self.password_input_2.move(175, 215)
        self.password_input_2.resize(275, 25)
        self.password_input_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.button = QPushButton(self)
        self.button.move(225, 275)
        self.button.resize(150, 25)
        self.button.setText('Готово')
        self.button.clicked.connect(self.add_info)
        self.button.setStyleSheet("QPushButton{\n"
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
        self.button_2.move(225, 525)
        self.button_2.resize(150, 25)
        self.button_2.setText('Сгенерировать пароль')
        self.button_2.clicked.connect(self.generate_password)
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

    def generate_password(self):
        self.length = []
        self.abc = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        for letter in self.abc:
            self.length.append(letter)
        shuffle(self.length)
        self.shuffled_password = ''.join(self.length[:10])
        self.password_input_2.setText(str(self.shuffled_password))

    def add_info(self):
        login_data = self.password_input.text()
        password_data = self.password_input_2.text()
        if len(login_data) == 0:
            return
        if len(password_data) < 8:
            return
        cursor.execute(f'SELECT login FROM info WHERE login="{login_data}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO info VALUES("{login_data}", "{password_data}")')
            self.status.setText(f'Аккаунт {login_data} успешно зарегистрирован!')
            db.commit()
        else:
            self.status.setText('Такая записать уже имеется!')
        cursor.close()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)


    def get_back(self):
        self.dialog.show()
        self.close()
