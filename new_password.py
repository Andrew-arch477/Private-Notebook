import sys
import sqlite3
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


class Save_Password(QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_login = QLineEdit(self)
        self.save_btn = QPushButton('Save')
        self.save_btn.setObjectName('btn')
        self.login_btn_back = QPushButton('Back')
        self.login_btn_back.setObjectName('btn')

        
        central_widget = QWidget()
        main_line = QVBoxLayout(central_widget)
        main_line.addWidget(self.new_login)
        main_line.addWidget(self.save_btn)
        main_line.addWidget(self.login_btn_back)

        self.save_btn.clicked.connect(self.save_new_login)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('NewPass')


    def save_new_login(self):
        con = sqlite3.connect("12.db")
        cursor = con.cursor()
        query_insert1 = f"""INSERT INTO Password (Password)
VALUES (?); """
        text = self.new_login.text()
        try:
            cursor.execute(query_insert1, '3')
            QMessageBox.information(self, 'Success', 'Text saved successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred while saving the file:\n{str(e)}')
