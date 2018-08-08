# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xml.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 190, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deal)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 90, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 141, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 111, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "make data"))
        self.pushButton.setText(_translate("Form", "生成数据"))
        self.label.setText(_translate("Form", "输入配置文件夹地址："))
        self.label_2.setText(_translate("Form", "请填写地址"))
        self.label_3.setText(_translate("Form", "输入生成数量："))

    def deal(self):
        sa = self.lineEdit.text()
        count = self.lineEdit_2.text()

        if str(sa).strip() == '':
            import os
            file_path = os.path.join(os.path.expanduser("~"), 'Desktop')
            file_path = str(file_path) + "//1"
            sa = file_path
        import Uc as uc
        uu = uc
        uu.file_p = sa
        uu.xml_path = sa + "\\生成结果\\"

        print(str(count) + ".........")
        if int(count) > 0:
            tmp_cot = int(count)
        if str(count).strip() == '':
            tmp_cot = 1000
        print(tmp_cot)
        uu.count = tmp_cot
        print(self.label_2.text())
        import threading
        threading.Thread(target=(self.uu_start), args=(uu,)).start()
        self.label_2.setText("数据生成中...稍等片刻")
        print("end")

    def uu_start(self, uu):
        uu.man()
        self.label_2.setText("生成完成")
