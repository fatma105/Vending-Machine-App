from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUiType
import os
from os import path
import sys
from PyQt5 import QtWidgets, uic, QtGui

FORRM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "SVM.ui"))

######intiate ui file############
class FirstClass(QMainWindow,FORRM_CLASS):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch)
        self.Handle_UI()
        # self.Handle_Button()


    def Handle_UI(self):
        self.setWindowTitle('Smart Vending Machine')
    def switch(self):
        stacked_widget.setCurrentIndex(1)


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "Home.ui"))
class SecondClass(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__()
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.Handle_product()


#when make  FORM_CLASS comment and active go_to_page2 it display configration of lcd only
#when make go_to_page2   comment and active  FORM_CLASS it display everything
    # def go_to_page2(self):
    #     loadUiType(path.join(path.dirname(__file__),"Home.ui"))
    def Handle_product(self):
        self.setWindowTitle('Page of Products')
        self.setWindowIcon(QIcon('./img/download (4).jpg'))
        # self.setMenuWidget()
        #ProductImage
        image_path=path.join(path.dirname(__file__),"./img/download (1).jpg")
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        self.pushButton_47.setIcon(icon)
        self.pushButton_47.setIconSize(QSize(100, 100))

        # ProductName
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setStyleSheet('color: black;')
        font = QtGui.QFont("Times New Roman", 14)
        self.pushButton_5.setFont(font)
        #price
        self.pushButton_6.setEnabled(False)
        font = QtGui.QFont("Times New Roman", 12)
        self.pushButton_6.setFont(font)
        #LCD
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.pushButton_13.clicked.connect(self.increaseNumber)

        self.pushButton_7.clicked.connect(self.decreaseNumber)

    def increaseNumber(self):
        num = int(self.lcdNumber_2.value())
        if num < 100:
            num += 1
            self.lcdNumber_2.display(num)

    def decreaseNumber(self):
        num = int(self.lcdNumber_2.value())
        if num > 0:
            num -= 1
            self.lcdNumber_2.display(num)

    def switch(self):
        stacked_widget.setCurrentIndex(0)

app = QApplication(sys.argv)
stacked_widget = QStackedWidget()
first_class = FirstClass()
second_class = SecondClass()
stacked_widget.addWidget(first_class)
stacked_widget.addWidget(second_class)
stacked_widget.show()
sys.exit(app.exec_())