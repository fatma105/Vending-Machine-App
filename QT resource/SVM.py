from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUiType
from os import path
import sys
import qrcode
import requests
# from machine.models import *
# from models import VendingMachine
# from models import initialize_machine
# machine=initialize_machine("machine@mail.com","123456")
from models import *


machine=None
machine=initialize_machine("machine@gmail.com","123456789")

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))

class Register(QMainWindow, FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_register()
        self.Handle_signup()
        

    def Handle_register(self):
        email = self.lineEdit_2.text()
        print(email)
        password = self.lineEdit_3.text()
        print(password)

    def Handle_signup(self):
        # if self.lineEdit_2.text() != "" or self.lineEdit_3.text() != "":
        self.LoginPButton.clicked.connect(self.Handle_register)
        self.LoginPButton.clicked.connect(self.switchLogin)

    def switchLogin(self):
        stacked_widget.setCurrentIndex(1)
FORRM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "SVM.ui"))
class introPage(QMainWindow,FORRM_CLASS):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Smart Vending Machine')
        self.centralwidget= QGridLayout()
        self.setLayout(self.centralwidget)
        self.LogoPB.clicked.connect(self.switch)
        # self.VendingMachine=machine
    def switch(self):
        if machine:
            stacked_widget.setCurrentIndex(1)
        else:
            stacked_widget.setCurrentIndex(2)
FORM_CLASS1, _ = loadUiType(path.join(path.dirname(__file__), "fixedpage.ui"))
class ProductClass(QMainWindow,FORM_CLASS1):
    def __init__(self,machine):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Page of Products')

        self.machine=machine
        self.products=self.machine.get_products()

        self.Handle_product1()
        self.Handle_product2()
        self.Handle_product3()
        self.Handle_product4()
        self.pushButton_5.clicked.connect(self.switch)
        self.Buy.clicked.connect(self.switchOrder)
        
    def Handle_product1(self):
                #ProductImage
                product1=self.products[0]
                url = product1.imgUrl
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label.setPixmap(scaled_pixmap)
                # Set the alignment of the label to center
                self.label.setAlignment(Qt.AlignCenter)

                # ProductName
                # product1=VendingMachine.get_product_by_slot(3)
                ProductName1=product1.name
                self.pushButton_49.setText(ProductName1)
                #price
                ProductPrice2 = f"Price:{product1.price}EGP"
                self.pushButton_50.setText(ProductPrice2)

                #LCD
                self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button.clicked.connect(self.increaseNumber)

                self.pushButton_7.clicked.connect(self.decreaseNumber)
    def increaseNumber(self):
        num=int(self.lcdNumber_2.value())

        if num < self.products[0].amount:
            num += 1
            self.lcdNumber_2.display(num)
    def decreaseNumber(self):
        num = int(self.lcdNumber_2.value())
        if num > 0:
            num -= 1
            self.lcdNumber_2.display(num)
    def Handle_product2(self):
                #ProductImage
                product2=self.products[1]
                url =product2.imgUrl
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label_2.setPixmap(scaled_pixmap)
                # Set the alignment of the label to center
                self.label_2.setAlignment(Qt.AlignCenter)

                # ProductName
                ProductName2=product2.name
                self.pushButton_51.setText(ProductName2)
                self.pushButton_51.setEnabled(False)
                #price
                ProductPrice2 = f"Price:{product2.price}EGP"
                self.pushButton_52.setText(ProductPrice2)
                #LCD
                self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_2.clicked.connect(self.increaseNumber2)

                self.pushButton_8.clicked.connect(self.decreaseNumber2)
    def increaseNumber2(self):
        num = int(self.lcdNumber_3.value())
        if num < self.products[1].amount:
            num += 1
            self.lcdNumber_3.display(num)
    def decreaseNumber2(self):
        num = int(self.lcdNumber_3.value())
        if num > 0:
            num -= 1
            self.lcdNumber_3.display(num)
    def Handle_product3(self):
                # ProductImage
                url = "https://firebasestorage.googleapis.com/v0/b/sigin-a0a4b.appspot.com/o/machine%2FFrozen%20food-pana.png?alt=media&token=d8392685-54b6-4ce6-8846-97b891b1e255"
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label_3.setPixmap(scaled_pixmap)
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
                url = "https://firebasestorage.googleapis.com/v0/b/sigin-a0a4b.appspot.com/o/machine%2FFrozen%20food-pana.png?alt=media&token=d8392685-54b6-4ce6-8846-97b891b1e255"
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label_4.setPixmap(scaled_pixmap)
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
        if machine:
            stacked_widget.setCurrentIndex(0)
        else:
            stacked_widget.setCurrentIndex(1)
    def switchOrder(self):
        
        amount1=int(self.lcdNumber_2.value())
        amount2=int(self.lcdNumber_3.value())
        amount3=int(self.lcdNumber_4.value())
        amount4=int(self.lcdNumber_5.value())
        if amount1:
            product=self.products[0]
            machine.add_item_to_cart(product,amount1)
        if amount2:
            product=self.products[1]
            machine.add_item_to_cart(product,amount2)
        if amount3:
            product=self.products[2]
            machine.add_item_to_cart(product,amount3)
        if amount4:
            product=self.products[3]
            machine.add_item_to_cart(product,amount4)   
        if machine:
            stacked_widget.setCurrentIndex(2)
        else:
            stacked_widget.setCurrentIndex(3)

FORM_CLASS2, _ = loadUiType(path.join(path.dirname(__file__), "order.ui"))

class CheckoutWindow(QMainWindow,FORM_CLASS2):
    def __init__(self,parent=None):
        super().__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_order()
        self.pushButton_back.clicked.connect(self.switchOrder)
        self.SubmitpushButton_5.clicked.connect(self.switchQRcode)


    def Handel_order(self):
        self.setWindowTitle('Checkout')
        #Date
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        date = formatted_datetime
        self.pushButton_2.setText(date)
        self.pushButton_2.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
        #list of products
        # if self.lcdNumber_2.value()!=0:
        # self.listWidget.addItems([])
        self.pushButton_2.setText(date)
        self.pushButton_2.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
        #total price
        total_price = "self.machine.order.total"
        self.pushButton_4.setText(total_price)
        self.pushButton_4.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
    def switchOrder(self):
        if machine:
            stacked_widget.setCurrentIndex(1)
        else:
            stacked_widget.setCurrentIndex(2)
    def switchQRcode(self):
        if machine:
            stacked_widget.setCurrentIndex(3)
        else:
            stacked_widget.setCurrentIndex(4)
                 
FORRM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "qr code.ui"))
class qrCodePage(QMainWindow,FORRM_CLASS):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.generateCode()
    def generateCode(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data('https://www.google.com.eg/?hl=ar')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode.png')
        pixmap = QPixmap('qrcode.png')
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setPixmap(pixmap)
        self.pushButton.clicked.connect(self.switchOrder)
    def switchOrder(self):
        if machine:
            stacked_widget.setCurrentIndex(2)
        else:
            stacked_widget.setCurrentIndex(3)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    first_class =Register()
    second_class = introPage()
    thrid_class = ProductClass(machine=machine)
    fourth_class= CheckoutWindow()
    fifth_class=qrCodePage()
    if machine:
        stacked_widget.addWidget(second_class)
        stacked_widget.addWidget(thrid_class)
        stacked_widget.addWidget(fourth_class)
        stacked_widget.addWidget(fifth_class)
    else:
        stacked_widget.addWidget(first_class)
        stacked_widget.addWidget(second_class)
        stacked_widget.addWidget(thrid_class)
        stacked_widget.addWidget(fourth_class)
        stacked_widget.addWidget(fifth_class)
    stacked_widget.show()
    sys.exit(app.exec_())

