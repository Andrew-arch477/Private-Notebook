import json
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
from login_window import LoginWindow
from test import Save_Password
from test_new import Enter_Save_Password
from digital_secuare_diary_or_notebook import Personal_Diary


def show_Word():
    try:
        
        connection = sqlite3.connect('12.db')
        cursor = connection.cursor()

        cursor.execute("SELECT Password FROM Password;")
        result = cursor.fetchone()

        if result and log_wind.login.text() == result[0]:
            log_wind.hide()
            word.show()
        else:
            QMessageBox.information(log_wind, 'Error', 'Wrong password!')

    except sqlite3.Error as e:
        QMessageBox.critical(None, 'Database Error', f'Database error: {e}')

    finally:
        
        if connection:
            connection.close()


def show_test():
    with open ('password_name.json') as file:
        data = json.load(file) 
    if enter_create.word_login.text() == data['word']:
        enter_create.hide()
        create.show()
    else:
        QMessageBox.information(log_wind, 'Error', 'Wrong password!')

def hide_Word():
    log_wind.show()
    word.hide()

def show_enter_password_window():
    log_wind.hide()
    enter_create.show()

def hide_enter_password_window():
    log_wind.show()
    enter_create.hide()


def hide_password_window():
    log_wind.show()
    create.hide()

def hide_word_back_to_login():
    log_wind.show()
    word.hide()

with open("styles.css", "r") as file:
    styles = file.read()

if __name__ == "__main__":
    app = QApplication([])
    
    log_wind = LoginWindow()
    word = Personal_Diary()
    create = Save_Password()
    enter_create = Enter_Save_Password()


    app.setStyleSheet(styles)

    log_wind.btn.clicked.connect(show_Word)
    log_wind.exit_btn.clicked.connect(log_wind.close)
    log_wind.create_password_btn.clicked.connect(show_enter_password_window)
    create.login_btn_back.clicked.connect(hide_password_window)
    enter_create.answer_btn.clicked.connect(show_test)
    enter_create.login_en_btn_back.clicked.connect(hide_enter_password_window)
    word.back_to_login.clicked.connect(hide_word_back_to_login)

    log_wind.show()
    app.exec()