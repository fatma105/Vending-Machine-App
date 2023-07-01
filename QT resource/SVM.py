from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUiType
import os
from os import path
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
FORRM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "SVM.ui"))

######intiate ui file############
class FirstClass(QMainWindow,FORRM_CLASS):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        # # Get the size of the user's screen
        # screen_size = QDesktopWidget().screenGeometry()
        # # Set the size of the window to fit the screen
        # self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.pushButton.clicked.connect(self.switch)
        self.Handle_UI()

    def Handle_UI(self):
        self.setWindowTitle('Smart Vending Machine')

    def switch(self):
        stacked_widget.setCurrentIndex(1)

FORM_CLASS1, _ = loadUiType(path.join(path.dirname(__file__), "fixedpage.ui"))
class ProductClass(QMainWindow,FORM_CLASS1):
    def __init__(self, parent=None):
        super().__init__()
        QMainWindow.__init__(self)

        self.setupUi(self)

        self.product_list = []  # create an empty list to store the product information
        self.setWindowTitle('Page of Products')
        self.Handle_product1()
        self.Handle_product2()
        self.Handle_product3()
        self.Handle_product4()
        # Get the size of the user's screen
        screen_size = QDesktopWidget().screenGeometry()
        # Set the size of the window to fit the screen
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.pushButton_5.clicked.connect(self.switch)
        self.pushButton_6.clicked.connect(self.switchOrder)
    def Handle_product1(self):
                #ProductImage
                image_path=path.join(path.dirname(__file__),"./img/download (1).jpg")
                pixmap = QPixmap(image_path)
                # Set the pixmap as the label's image
                self.label.setPixmap(pixmap)

                # Resize the label to fit the image
                # self.label.resize(100, 100)

                # Set the alignment of the label to center
                self.label.setAlignment(Qt.AlignCenter)
                # ProductName
                ProductName1="chipsy"
                self.pushButton_49.setText(ProductName1)
                #price
                ProductPrice2 = "Price:07$"
                self.pushButton_50.setText(ProductPrice2)

                #LCD
                self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button.clicked.connect(self.increaseNumber)

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
    def Handle_product2(self):
                #ProductImage
                image_path=path.join(path.dirname(__file__),"./img/download (2).jpg")
                pixmap = QPixmap(image_path)
                # Set the pixmap as the label's image
                self.label_2.setPixmap(pixmap)

                # Resize the label to fit the image
                # self.label_2.resize(100,80 )
                # Set the alignment of the label to center
                self.label_2.setAlignment(Qt.AlignCenter)

                # ProductName
                ProductName2="Beak"
                self.pushButton_51.setText(ProductName2)
                self.pushButton_51.setEnabled(False)
                #price
                ProductPrice2 = "Price:10$"
                self.pushButton_52.setText(ProductPrice2)
                #LCD
                self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_2.clicked.connect(self.increaseNumber2)

                self.pushButton_8.clicked.connect(self.decreaseNumber2)
    def increaseNumber2(self):
        num = int(self.lcdNumber_3.value())
        if num < 100:
            num += 1
            self.lcdNumber_3.display(num)
    def decreaseNumber2(self):
        num = int(self.lcdNumber_3.value())
        if num > 0:
            num -= 1
            self.lcdNumber_3.display(num)
    def Handle_product3(self):
                #ProductImage
                image_path=path.join(path.dirname(__file__),"./img/download (3).jpg")
                pixmap = QPixmap(image_path)
                # Set the pixmap as the label's image
                self.label_3.setPixmap(pixmap)

                # Resize the label to fit the image
                # self.label_3.resize(100,80 )
                # Set the alignment of the label to center
                self.label_3.setAlignment(Qt.AlignCenter)
                # ProductName
                ProductName3="Lambada"
                self.pushButton_53.setText(ProductName3)
                self.pushButton_53.setEnabled(False)
                #price
                ProductPrice3 = "Price:05$"
                self.pushButton_54.setText(ProductPrice3)
                #LCD
                self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_3.clicked.connect(self.increaseNumber3)

                self.pushButton_9.clicked.connect(self.decreaseNumber3)
    def increaseNumber3(self):
        num = int(self.lcdNumber_4.value())
        if num < 100:
            num += 1
            self.lcdNumber_4.display(num)
    def decreaseNumber3(self):
        num = int(self.lcdNumber_4.value())
        if num > 0:
            num -= 1
            self.lcdNumber_4.display(num)
    def Handle_product4(self):
                #ProductImage
                image_path=path.join(path.dirname(__file__),"./img/download (4).jpg")
                pixmap = QPixmap(image_path)
                # Set the pixmap as the label's image
                self.label_4.setPixmap(pixmap)

                # Resize the label to fit the image
                # self.label_4.resize(100,80 )
                # Set the alignment of the label to center
                self.label_4.setAlignment(Qt.AlignCenter)
                # ProductName
                ProductName4="Galaxy"
                self.pushButton_55.setText(ProductName4)
                self.pushButton_55.setEnabled(False)
                #price
                ProductPrice4 = "Price:20$"
                self.pushButton_56.setText(ProductPrice4)
                self.pushButton_56.setEnabled(False)
                #LCD
                self.lcdNumber_5.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_4.clicked.connect(self.increaseNumber4)

                self.pushButton_10.clicked.connect(self.decreaseNumber4)
    def increaseNumber4(self):
        num = int(self.lcdNumber_5.value())
        if num < 100:
            num += 1
            self.lcdNumber_5.display(num)
    def decreaseNumber4(self):
        num = int(self.lcdNumber_5.value())
        if num > 0:
            num -= 1
            self.lcdNumber_5.display(num)
    def switch(self):
        stacked_widget.setCurrentIndex(0)
    def switchOrder(self):
        stacked_widget.setCurrentIndex(2)

FORM_CLASS2, _ = loadUiType(path.join(path.dirname(__file__), "order.ui"))

class CheckoutWindow(QMainWindow,FORM_CLASS2):
    def __init__(self,parent=None):
        super().__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_order()

        self.pushButton_back.clicked.connect(self.switchOrder)
    def Handel_order(self):
        self.setWindowTitle('Checkout')
        #Date
        date = "10/10"
        self.pushButton_2.setText(date)
        self.pushButton_2.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
        #list of products
        self.listWidget.addItems(['Item 1', 'Item 2', 'Item 3'])
        #total price
        total_price = "100$"
        self.pushButton_4.setText(total_price)
        self.pushButton_4.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
    def switchOrder(self):
        stacked_widget.setCurrentIndex(1)

app = QApplication(sys.argv)
stacked_widget = QStackedWidget()
first_class = FirstClass()
second_class = ProductClass()
thrid_class = CheckoutWindow()
stacked_widget.addWidget(first_class)
stacked_widget.addWidget(second_class)
stacked_widget.addWidget(thrid_class)
stacked_widget.show()
sys.exit(app.exec_())

