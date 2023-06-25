from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUiType
from os import path

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))

class Register(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_register()
        self.Handle_signup()

    def Handle_register(self):
        email=self.lineEdit_2.text()
        print(email)
        password =self.lineEdit_3.text()
        print(password)
    def Handle_signup(self):
        self.pushButton_3.clicked.connect(self.Handle_register)


if __name__ == '__main__':
    app = QApplication([])
    stacked_widget = QStackedWidget()
    third_class = Register()
    stacked_widget.addWidget(third_class)
    stacked_widget.show()
    app.exec_()