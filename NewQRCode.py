# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QRCode.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# importation de qrcode et de pillow
import qrcode
from PIL.ImageQt import ImageQt

# importation de la pixmap
from PyQt5.QtGui import QPixmap 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 353)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 291, 231))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 260, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Inserer un Texte pour generer le QR Code</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton_2.setText(_translate("Form", "Effacer"))
        self.pushButton.clicked.connect(self.generQRCode)
        self.pushButton_2.clicked.connect(self.Effacer)
    
    # Methode generation de code
    def generQRCode(self):
        #recuperation du texte
        TextSaisie = print(self.textEdit.toPlainText())
        
        #creation d'un qrcode en image
        img = qrcode.make(TextSaisie)
        qr = ImageQt(img)
        
        #creation de la pixmap
        pix = QPixmap.fromImage(qr)
        
        #afficher l'image
        self.label.setPixmap(pix)
        
    # Methode Effacer
    def Effacer(self):
        self.textEdit.setText("")
        self.label.setText("Inserer un Texte pour generer le QR Code")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())    

