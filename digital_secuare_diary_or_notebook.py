import sys
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
    QFileDialog
)


class Personal_Diary(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.save_btn = QPushButton("Save")
        self.save_btn.setObjectName('btn')
        self.load_btn = QPushButton("Load")
        self.load_btn.setObjectName('btn')
        self.back_to_login = QPushButton("Back")
        self.back_to_login.setObjectName('btn')

        self.save_btn.clicked.connect(self.save_text)
        self.load_btn.clicked.connect(self.load_text)

        main_line = QWidget()
        layout = QVBoxLayout(main_line)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.load_btn)

        self.setCentralWidget(main_line)
        self.setWindowTitle('My diary')


    def load_text(self):
        file_name = QFileDialog.getOpenFileName(self)[0]
        if file_name:
            try:
                with open(file_name) as file:
                    text = file.read()
                    self.text_edit.setPlainText(text)
                QMessageBox.information(self, 'Success', 'Text loaded successfully.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An error occurred while loading the file:\n{str(e)}')

    def save_text(self):
        text = self.text_edit.toPlainText()
        file_name = QFileDialog.getSaveFileName(self)[0]
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    file.write(text)
                QMessageBox.information(self, 'Success', 'Text saved successfully.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An error occurred while saving the file:\n{str(e)}')



        
