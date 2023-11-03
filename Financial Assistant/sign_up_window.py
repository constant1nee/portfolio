from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5 import QtGui
from menu_window import MenuWindow
import sqlite3

class SignUpWindow(QMainWindow):
    def __init__(self, dialog):
        self.dialog = dialog
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText('Вход')
        self.label.move(280, 175)
        self.label.resize(35, 15)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color: #aebccf')

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Financial Assistant (Вход)')

        self.label_1 = QLabel(self)
        self.label_1.move(105, 240)
        self.label_1.resize(50, 15)
        self.label_1.setText('Логин:')
        font = QtGui.QFont()
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet('background-color: #aebccf')

        self.label_2 = QLabel(self)
        self.label_2.move(105, 290)
        self.label_2.resize(60, 15)
        self.label_2.setText('Пароль:')
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: #aebccf')

        self.status = QLabel(self)
        self.status.move(115, 400)
        self.status.resize(150, 50)
        font = QtGui.QFont()
        font.setBold(True)
        self.status.setFont(font)

        self.password_input = QLineEdit(self)
        self.password_input.move(175, 240)
        self.password_input.resize(275, 25)
        self.password_input.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.password_input_2 = QLineEdit(self)
        self.password_input_2.move(175, 290)
        self.password_input_2.resize(275, 25)
        self.password_input_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 6px;\n"
                                      "    background-color: #aebccf;\n"
                                      "    border: 2px solid #0b3a73;\n"
                                      "    color: #0b3a73;\n"
                                      "}\n"
                                      "")

        self.button = QPushButton(self)
        self.button.move(225, 340)
        self.button.resize(150, 25)
        self.button.setText('Готово')
        self.button.clicked.connect(self.get_access)
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

    def get_access(self):
        db = sqlite3.connect('fin_assist.db')
        cursor = db.cursor()
        user_login = self.password_input.text()
        user_password = self.password_input_2.text()
        if len(user_login) == 0:
            return
        if len(user_password) < 8:
            return
        try:
            cursor.execute(f'SELECT password FROM info WHERE login="{user_login}"')
            check_password = cursor.fetchall()
            cursor.execute(f'SELECT login FROM info WHERE login="{user_login}"')
            check_login = cursor.fetchall()
            if check_password[0][0] == user_password and check_login[0][0] == user_login:
                self.status.setText('Успешная авторизация!')
                self.dialog = MenuWindow(self)
                self.dialog.show()
                self.hide()
            else:
                self.status.setText('Ошибка авторизации!')
        except:
            self.status.setText('Ошибка авторизации!')
        cursor.close()

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QPainter(self)
        pixmap = QPixmap("./finance.jpg")
        painter.drawPixmap(self.rect(), pixmap)


    def get_back(self):
        self.dialog.show()
        self.close()