# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Train60DaysDownload2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import  QDate

from datetime import date
from datetime import timedelta


url = 'http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/railway_schedule/XML/list'



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        # icon = QIcon(TrainLogosvg())
        icon = QIcon('TRALogo2.svg')
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 611, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")        
        self.today = date.today()
        self.today_year = int(self.today.strftime("%Y"))
        self.today_mounth = int(self.today.strftime("%m"))
        self.today_day = int(self.today.strftime("%d"))

        self.endmyday = self.today+timedelta(days=59)
        self.endmyday_year = int(self.endmyday.strftime("%Y"))
        self.endmyday_mounth = int(self.endmyday.strftime("%m"))
        self.endmyday_day = int(self.endmyday.strftime("%d"))
        
        self.dateEdit.setDate(QDate(self.today_year,self.today_mounth,self.today_day)) #在日曆上選擇今日日期
        self.dateEdit.setMinimumDate(QDate(self.today_year,self.today_mounth,self.today_day))#將日曆上過去日期disabled 掉       
        self.dateEdit.setMaximumDate(QDate(self.endmyday_year,self.endmyday_mounth,self.endmyday_day))#將日曆上未來日期disabled 掉 

        self.verticalLayout_6.addWidget(self.dateEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True) 
        self.radioButton.setObjectName("radioButton")        
        self.verticalLayout_7.addWidget(self.radioButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_8.addWidget(self.radioButton_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_10.addWidget(self.radioButton_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_9.addWidget(self.radioButton_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_5.addWidget(self.radioButton_5)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")



        self.horizontalLayout_5.addWidget(self.spinBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(630, 70, 160, 143))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        font2 = QtGui.QFont()
        font2.setFamily("微軟正黑體")
        font2.setPointSize(16)
        font2.setBold(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet('QPushButton {background-color: red ; color: white;}')
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_16.addWidget(self.pushButton_3)
        font3 = QtGui.QFont()
        font3.setFamily("微軟正黑體")
        font3.setPointSize(16)
        font3.setBold(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet('QPushButton {background-color: blue ; color: white;}')
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.clicked.connect(self.Buttonclicked_OK)
        self.verticalLayout_16.addWidget(self.pushButton_2)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('QPushButton {background-color: #550088 ; color: white;}')
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.ButtonclickedExit)
        self.verticalLayout_16.addWidget(self.pushButton)        
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 781, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(240, 0))
        self.label_4.setMaximumSize(QtCore.QSize(240, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setMinimumSize(QtCore.QSize(240, 0))
        self.label_5.setMaximumSize(QtCore.QSize(240, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar.setMinimumSize(QtCore.QSize(240, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(240, 16777215))
        # self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 270, 781, 291))
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 781, 261))
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setObjectName("tableView")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableView.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage(' ')

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "台鐵網路列車時刻下載"))
        self.label.setText(_translate("MainWindow", "台鐵網路列車時刻下載"))
        self.label_2.setText(_translate("MainWindow", "請選擇起始日期："))
        self.label_3.setText(_translate("MainWindow", "請設定下載天數："))

        self.radioButton.setText(_translate("MainWindow", "2天"))
        self.radioButton_2.setText(_translate("MainWindow", "7天"))
        self.radioButton_3.setText(_translate("MainWindow", "30天"))
        self.radioButton_4.setText(_translate("MainWindow", "60天"))

        self.pushButton_3.setText(_translate("MainWindow", "停止下載"))
        self.pushButton_2.setText(_translate("MainWindow", "開始下載"))
        self.pushButton.setText(_translate("MainWindow", "結束程式"))
        self.label_4.setText(_translate("MainWindow", "系統下載顯示訊息："))
        self.label_5.setText(_translate("MainWindow", " "))
        self.groupBox.setTitle(_translate("MainWindow", "下載完成列表："))
 