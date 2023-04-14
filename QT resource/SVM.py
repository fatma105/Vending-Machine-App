from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUiType
import os
from os import path
import sys
############import ui file###########

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "SVM.ui"))

######intiate ui file############
class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Button()

    def Handle_UI(self):
        self.setWindowTitle('Smart Vending Machine')

#logo this is name for logo PushButton ,i changed it in qt designer
    def Handle_Button(self):
        page=NextPage().go_to_page2()
        self.logo.clicked.connect(page)


#the next page "Home page"
class NextPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(NextPage, self).__init__()
        self.go_to_page2()
        self.Handle_lcd()
        #self.show()

    def go_to_page2(self):
        loadUiType(path.join(path.dirname(__file__),"Home.ui"))

    def Handle_lcd(self):
        # Create LCD Number and set its properties
        self.lcd = QLCDNumber(self)
        self.lcd.display(0)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setFixedSize(50, 50)

        # Create Plus Button and set its properties
        self.plus_button = QPushButton("+", self)
        self.plus_button.setFixedSize(30, 30)
        self.plus_button.clicked.connect(self.increaseNumber)
        # Create Subtract Button and set its properties
        self.subtract_button = QPushButton("-", self)
        self.subtract_button.setFixedSize(30, 30)
        self.subtract_button.clicked.connect(self.decreaseNumber)
        # Create horizontal Box Layout and add widgets to it
        hbox = QVBoxLayout()
        hbox.addWidget(self.lcd)
        hbox.addWidget(self.plus_button)
        hbox.addWidget(self.subtract_button)
        self.setLayout(hbox)

    def increaseNumber(self):
        num = int(self.lcd.value())
        if num < 100:
            num += 1
            self.lcd.display(num)

    def decreaseNumber(self):
        num = int(self.lcd.value())
        if num > 0:
            num -= 1
            self.lcd.display(num)

def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    # Nextwindow=NextPage()
    # Nextwindow.show()
    app.exec_()
if __name__=='__main__':
    main()