from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QFileDialog, 
    QTextEdit
    )

def open_file():
    file_path = QFileDialog.getOpenFileName(window)[0]
    with open(file_path) as file:
        content = file.read()
    return content

def show_content():
    content = open_file()
    text.setText(content)

def create_file(path, content):
    with open(path, "w") as file:
        file.write(content)

def save_content():
    path = QFileDialog.getSaveFileName(window)[0]
    content = text.toPlainText()
    create_file(path, content)

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()

    text = QTextEdit(window)

    save = QPushButton(window)
    save.setText("Save")
    save.move(100, 300)

    load = QPushButton(window)
    load.setText("Load")
    load.move(10, 300)

    save.clicked.connect(save_content)
    load.clicked.connect(show_content)


    window.show()
    app.exec()