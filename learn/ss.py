# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ss.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(20, 0, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 70, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 270, 75, 23))
        self.pushButton.setIconSize(QtCore.QSize(30, 16))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.radioButton.clicked.connect(self.calendarWidget.showNextYear)
        self.pushButton.clicked.connect(self.pri)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.pushButton.setText(_translate("Form", "PushButton"))

    def pri(self):
        print("ok")
