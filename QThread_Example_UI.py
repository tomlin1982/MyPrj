# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui , QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 331)
        self.runButton = QtWidgets.QPushButton(Form)
        self.runButton.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.runButton.setObjectName("runButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 431, 192))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qthread Example"))
        self.runButton.setText(_translate("Form", "Run"))