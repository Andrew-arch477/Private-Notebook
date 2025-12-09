from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import ( 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QRadioButton,
    QGroupBox,
    QPushButton,
    QLineEdit
)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.login = QLineEdit()

        self.Hallo_password_text = QLabel("Hallo! And welcome to a personal diary. \n Enter your password please.")
        self.Hallo_password_text.setObjectName('Hallo')
        self.Hallo_password_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.new_pass = QLabel("(If you don't have password click on this button to create it.)")

        self.btn = QPushButton("Enter")
        self.btn.setObjectName('btn')

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.setObjectName('btn')

        self.create_password_btn = QPushButton("Create password")
        self.create_password_btn.setObjectName('btn')

        main_line = QVBoxLayout()

        main_line.addWidget(self.Hallo_password_text)
        main_line.addWidget(self.login)
        main_line.addWidget(self.btn)
        main_line.addWidget(self.exit_btn)
        main_line.addWidget(self.new_pass)
        main_line.addWidget(self.create_password_btn)


        self.setLayout(main_line)
        self.setWindowTitle('Access')

