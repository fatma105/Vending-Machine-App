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
        Open_page=NextPage()
        page=Open_page.go_to_page2()
        self.logo.clicked.connect(page)


#the next page "Home page"
class NextPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(NextPage, self).__init__()
        self.go_to_page2()
        self.show()

    def go_to_page2(self):
       uic.loadUi('Home.ui', self)

def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()