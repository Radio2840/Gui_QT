# Form implementation generated from reading ui file 'Layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_buttonClickMe(object):
    def setupUi(self, buttonClickMe):
        buttonClickMe.setObjectName("buttonClickMe")
        buttonClickMe.resize(400, 300)
        self.labelResponse = QtWidgets.QLabel(parent=buttonClickMe)
        self.labelResponse.setGeometry(QtCore.QRect(10, 10, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.labelResponse.setFont(font)
        self.labelResponse.setObjectName("labelResponse")
        self.label = QtWidgets.QLabel(parent=buttonClickMe)
        self.label.setGeometry(QtCore.QRect(20, 50, 351, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(parent=buttonClickMe)
        self.lineEditName.setGeometry(QtCore.QRect(80, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.pushButton = QtWidgets.QPushButton(parent=buttonClickMe)
        self.pushButton.setGeometry(QtCore.QRect(310, 250, 81, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(buttonClickMe)
        QtCore.QMetaObject.connectSlotsByName(buttonClickMe)

    def retranslateUi(self, buttonClickMe):
        _translate = QtCore.QCoreApplication.translate
        buttonClickMe.setWindowTitle(_translate("buttonClickMe", "Dialog"))
        self.labelResponse.setText(_translate("buttonClickMe", "Enter your name:"))
        self.pushButton.setText(_translate("buttonClickMe", "Submit"))
