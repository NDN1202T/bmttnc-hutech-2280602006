# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RSA(object):
    def setupUi(self, RSA):
        RSA.setObjectName("RSA")
        RSA.resize(1079, 605)
        self.centralwidget = QtWidgets.QWidget(RSA)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(180, 80, 241, 71))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 61, 16))
        self.label_3.setObjectName("label_3")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(180, 270, 241, 71))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(720, 270, 241, 71))
        self.txt_signature.setObjectName("txt_signature")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 300, 47, 13))
        self.label_4.setObjectName("label_4")
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(QtCore.QRect(720, 80, 241, 71))
        self.txt_information.setObjectName("txt_information")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 110, 51, 16))
        self.label_5.setObjectName("label_5")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(110, 410, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(310, 410, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(880, 420, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(680, 420, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(480, 430, 75, 23))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        RSA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RSA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        RSA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RSA)
        self.statusbar.setObjectName("statusbar")
        RSA.setStatusBar(self.statusbar)

        self.retranslateUi(RSA)
        QtCore.QMetaObject.connectSlotsByName(RSA)

    def retranslateUi(self, RSA):
        _translate = QtCore.QCoreApplication.translate
        RSA.setWindowTitle(_translate("RSA", "RSA"))
        self.label.setText(_translate("RSA", "RSA"))
        self.label_2.setText(_translate("RSA", "Pain text:"))
        self.label_3.setText(_translate("RSA", "Cipher text:"))
        self.label_4.setText(_translate("RSA", "Signature"))
        self.label_5.setText(_translate("RSA", "Information"))
        self.btn_encrypt.setText(_translate("RSA", "PushButton"))
        self.btn_decrypt.setText(_translate("RSA", "PushButton"))
        self.btn_verify.setText(_translate("RSA", "PushButton"))
        self.btn_sign.setText(_translate("RSA", "PushButton"))
        self.btn_gen_keys.setText(_translate("RSA", "Generate key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RSA = QtWidgets.QMainWindow()
    ui = Ui_RSA()
    ui.setupUi(RSA)
    RSA.show()
    sys.exit(app.exec_())
