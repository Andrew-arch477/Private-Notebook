import sys
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
    QRadioButton,
    QGroupBox,
    QPushButton,
    QLineEdit,
    QMessageBox,
    QListWidget
)


class Enter_Save_Password(QMainWindow):
    def __init__(self):
        super().__init__()

        with open("password.json", "r", encoding="utf-8") as file:
            self.data = dict(json.load(file))

        self.word_login = QLineEdit(self)
        self.answer_btn = QPushButton('Answer')
        self.answer_btn.setObjectName('btn1')
        self.login_en_btn_back = QPushButton('Back')
        self.login_en_btn_back.setObjectName('btn1')
        self.qustion = QLabel("Who is my favourite historical person?")

        
        central_widget = QWidget()
        main_line = QVBoxLayout(central_widget)
        main_line.addWidget(self.qustion)
        main_line.addWidget(self.word_login)
        main_line.addWidget(self.answer_btn)
        main_line.addWidget(self.login_en_btn_back)


        self.setCentralWidget(central_widget)
        self.setWindowTitle('Frase')


        



