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
import Hardware


machine=None
machine=initialize_machine("machine4@gmail.com","123456789")

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
                product3=self.products[2]
                url = product3.imgUrl
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label_3.setPixmap(scaled_pixmap)
                # Set the alignment of the label to center
                self.label_3.setAlignment(Qt.AlignCenter)

                # ProductName
                ProductName3=product3.name
                self.pushButton_53.setText(ProductName3)
                self.pushButton_53.setEnabled(False)
                #price
                ProductPrice3 = f"Price:{product3.price}EGP"
                self.pushButton_54.setText(ProductPrice3)
                #LCD
                self.lcdNumber_4.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_3.clicked.connect(self.increaseNumber3)

                self.pushButton_9.clicked.connect(self.decreaseNumber3)
    def increaseNumber3(self):
        num = int(self.lcdNumber_4.value())
        if num < self.products[2].amount:
            num += 1
            self.lcdNumber_4.display(num)
    def decreaseNumber3(self):
        num = int(self.lcdNumber_4.value())
        if num > 0:
            num -= 1
            self.lcdNumber_4.display(num)
    def Handle_product4(self):
                #ProductImage
                product4=self.products[3]
                url =product4.imgUrl
                response = requests.get(url)
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                scaled_pixmap = pixmap.scaled(200, 200)
                self.label_4.setPixmap(scaled_pixmap)
                # Set the alignment of the label to center
                self.label_4.setAlignment(Qt.AlignCenter)
                # ProductName
                ProductName4=product4.name
                self.pushButton_55.setText(ProductName4)
                self.pushButton_55.setEnabled(False)
                #price
                ProductPrice4 = f"Price:{product4.price}EGP"
                self.pushButton_56.setText(ProductPrice4)
                self.pushButton_56.setEnabled(False)
                #LCD
                self.lcdNumber_5.setSegmentStyle(QLCDNumber.Flat)

                self.plus_button_4.clicked.connect(self.increaseNumber4)

                self.pushButton_10.clicked.connect(self.decreaseNumber4)
    def increaseNumber4(self):
        num = int(self.lcdNumber_5.value())
        if num < self.products[3].amount:
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
    def takeOrder(self):
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
    def clearLCD(self):
        self.lcdNumber_2.display('')
        self.lcdNumber_3.display('')
        self.lcdNumber_4.display('')
        self.lcdNumber_5.display('')


              
    def switchOrder(self):
        self.takeOrder()
        if machine.order.items:
            stacked_widget.setCurrentIndex(2)
      

        #handle order in a different function

        #disable but button while no order
        
       

FORM_CLASS2, _ = loadUiType(path.join(path.dirname(__file__), "order.ui"))

class CheckoutWindow(QMainWindow,FORM_CLASS2):
    def __init__(self,machine,parent=None):
        super().__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.machine=machine
        self.Handel_order()
        self.pushButton_back.clicked.connect(self.switchOrder)
        


    def Handel_order(self):
        self.setWindowTitle('Checkout')
        #Date
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        date = formatted_datetime
        self.pushButton_2.setText(date)
        self.pushButton_2.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")

    def showOrder(self):
        if self.machine.order.items:
            order_data = machine.view_cart()
            #total price
            total_price =f"{self.machine.order.total}EGP"
            self.pushButton_4.setText(total_price)
            self.pushButton_4.setStyleSheet("color: black;background-color: rgb(255, 255, 255);")
            for item in order_data:
                self.listWidget.addItem(str(item))
    
    def switchOrder(self):
        if machine.order.items:
            self.listWidget.clear()
            machine.clear_cart()
            stacked_widget.setCurrentIndex(1)
        else:
            stacked_widget.setCurrentIndex(2)
    def switchQRcode(self):
        if machine.order.items:
            machine.save_order()
            machine.initialize_process_order()
            self.listWidget.clear()
            stacked_widget.setCurrentIndex(3)
        else:
            stacked_widget.setCurrentIndex(4)
                 
FORRM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "qr code.ui"))
class qrCodePage(QMainWindow,FORRM_CLASS):
    def __init__(self,machine):
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.machine=machine
        #self.generateCode()
    def generateCode(self):
        qr_info=machine.get_order_qrinfo()
        if qr_info:
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_info)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save('qrcode.png')
            pixmap = QPixmap('qrcode.png')
            self.label_2.setAlignment(Qt.AlignCenter)
            self.label_2.setPixmap(pixmap)
            self.pushButton.clicked.connect(self.switchOrder)
    def handel_payment(self):
        self.payment_worker=PaymentWorker()
        self.payment_worker.start()
        self.payment_worker.finished.connect(self.payment_worker_finished)
        self.payment_worker.update_status.connect(self.update_lable)
        

    def payment_worker_finished(self):
        stacked_widget.setCurrentIndex(0)


    def update_lable(self,text):
        self.label.setText('Scan Me')   
        self.label_2.setText(text)       

    def switchOrder(self):
        if machine:
            stacked_widget.setCurrentIndex(2)
        else:
            stacked_widget.setCurrentIndex(3)


#payment handler
class PaymentWorker(QThread):

    update_status=pyqtSignal(str)

    def run(self):
        machine.listen_to_order_status()
        i=True
        while i==True:
            status=machine.get_order_status()
            time.sleep(0.1)
            if status==10:
                self.update_status.emit("QR SCANNED PROCESSING PAYMENT....")
            elif status == 20:
                self.update_status.emit("PAYMENT SUCCESS,DISPENSING ITEMS....")
                #hardware logic here
                order_list=machine.create_order_list()
                print(order_list)
                Hardware.dispense_items(order_list)
                machine.update_stock()
                machine.clear_cart()
                machine.clear_process_order()
                time.sleep(3)
                break
            elif status == 30:
                self.update_status.emit("PAYMENT FAILED....")
                machine.clear_cart()
                machine.clear_process_order()
                time.sleep(3)
                break
            elif status == 100:
                self.update_status.emit("PROCESS TIME OUT")
                machine.clear_cart()
                machine.clear_process_order()
                time.sleep(3)
                break   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    first_class =Register()
    second_class = introPage()
    thrid_class = ProductClass(machine=machine)
    fourth_class= CheckoutWindow(machine)
    fifth_class=qrCodePage(machine)
    
    stacked_widget.addWidget(second_class)
    stacked_widget.addWidget(thrid_class)
    stacked_widget.addWidget(fourth_class)
    stacked_widget.addWidget(fifth_class)

    thrid_class.Buy.clicked.connect(thrid_class.switchOrder)
    thrid_class.Buy.clicked.connect(fourth_class.showOrder)
    fourth_class.SubmitpushButton_5.clicked.connect(thrid_class.clearLCD)
    fourth_class.SubmitpushButton_5.clicked.connect(fourth_class.switchQRcode)
    fourth_class.SubmitpushButton_5.clicked.connect(fifth_class.generateCode)
    fourth_class.SubmitpushButton_5.clicked.connect(fifth_class.handel_payment)
    

    stacked_widget.show()
    sys.exit(app.exec_())

