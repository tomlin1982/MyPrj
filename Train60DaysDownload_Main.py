# -*- coding: utf-8 -*-

import sys
import time
import numpy
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from os import listdir, remove, path, mkdir
from os.path import isfile, isdir, join
from PyQt5.QtCore import QProcess

from Train60DaysDownload_UI import Ui_MainWindow
import TrainDataXMLDownloader

folderpath = 'Downloads' #下載檔案的位置

if not path.isdir(folderpath):
    mkdir(folderpath)
else:
    pass

dir_files = listdir(folderpath)
for f in dir_files:      
  fullpath = join(folderpath, f)
  print(fullpath)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("檔案：", f)
    remove(fullpath)
  else:
      pass

url = 'http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/railway_schedule/XML/list'

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.work = WorkThread()


        self.pushButton_2.clicked.connect(self.execute)
        self.pushButton_3.clicked.connect(self.stop)
        self.pushButton.clicked.connect(self.Exit)

    def execute(self):
        dir_files = listdir(folderpath)
        for f in dir_files:     
            fullpath = join(folderpath, f)
            print(fullpath)
            # 判斷 fullpath 是檔案還是目錄
            if isfile(fullpath):
                print("檔案：", f)
                remove(fullpath)
            else:
                pass

        # 启动线程
        self.work.start()
        # 线程自定义信号连接的槽函数
        self.work.trigger.connect(self.display)

    def stop(self):
        self.work.quit()

    def Exit(self):
        sys.exit(self)

    def bar_progress(self, current, total, width=80):
        self.progressBar.setProperty("value", current / total * 100)      
        # progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
        # # Don't use print() as it will print in new line every time.
        # sys.stdout.write("\r" + progress_message)
        # sys.stdout.flush()

    def display(self):
        self.curratedate = self.dateEdit.date()
        self.curratedate_year_temp = self.curratedate.year()
        self.curratedate_month_temp = self.curratedate.month()
        self.curratedate_day_temp = self.curratedate.day()  
        self.curratedate_year = str(self.curratedate_year_temp)
        self.mydata = TrainDataXMLDownloader.XMLReader(url, folderpath)
        self.mydata.readdata()
        self.file_index_1 = self.mydata.retrunfile_index()
        self.reverse_file_index_1 = self.mydata.returnreverse_file_index()
        self.filedownload_path_index = self.mydata.returnfiledownload_path()  
        if self.curratedate_month_temp < 10:
            self.curratedate_month = str(0)+str(self.curratedate_month_temp)
        else:
            self.curratedate_month = str(self.curratedate_month_temp)
        
        if self.curratedate_day_temp < 10:
            self.curratedate_day = str(0)+str(self.curratedate_day_temp)
        else:
            self.curratedate_day = str(self.curratedate_day_temp)
        
        self.startdownloadfile = self.curratedate_year+self.curratedate_month+self.curratedate_day+'.xml'
        print(self.startdownloadfile)

        if self.radioButton.isChecked():
            # print(self.radioButton.text())
            self.counterdays = int(self.radioButton.text()[0:1])

        elif self.radioButton_2.isChecked():
            # print(self.radioButton_2.text())
            self.counterdays = int(self.radioButton_2.text()[0:1])

        elif self.radioButton_3.isChecked():
            # print(self.radioButton_3.text())
            self.counterdays = int(self.radioButton_3.text()[0:2])

        elif self.radioButton_4.isChecked():
            # print(self.radioButton_4.text())
            self.counterdays = int(self.radioButton_4.text()[0:2])

        elif self.radioButton_5.isChecked():
            self.counterdays = int(self.spinBox.value())
        else:
            self.counterdays = 7
        
        enddate = self.curratedate.addDays(self.counterdays)    
        

        # print(self.file_index_1.get('60'))
        maxdate_temp = self.file_index_1.get('60')[0:8]
        # print(maxdate)
        maxdate_year  = int(maxdate_temp[0:4])
        # print(maxdate_year)
        maxdate_month = int(maxdate_temp[4:6])
        # print(maxdate_month)
        maxdate_day = int(maxdate_temp[6:8])
        # print(maxdate_day)
        maxdate = datetime(maxdate_year, maxdate_month, maxdate_day)

        print(maxdate)
        self.downloadfile = []
        if maxdate > enddate:            
            print('a')
            start_index = int(self.reverse_file_index_1.get(self.startdownloadfile))
            print(enddate)
            print(start_index)
            end_index = int(self.counterdays)+start_index
            print(end_index)
            for key in range(start_index, end_index):
                print(key)
                print(self.file_index_1.get(str(key)))
                self.downloadfile.append(self.file_index_1.get(str(key)))

        elif maxdate < enddate:
            print('b')
            print(enddate)            
            print(self.counterdays+1)
            start_index = int(self.reverse_file_index_1.get(self.startdownloadfile))
            print(start_index)
            for key in range(start_index, 61):
                print(key)
                print(self.file_index_1.get(str(key)))
                self.downloadfile.append(self.file_index_1.get(str(key)))
        elif maxdate == enddate:
            print('c')
            print(enddate)
            print(start_index)
            print(self.counterdays+1)
            if (enddate - maxdate == timedelta(days=60)):
                for key in range(1, 61):
                    self.downloadfile.append(self.file_index_1.get(str(key)))
            elif (enddate - maxdate == timedelta(days=30)):
                start_index = int(self.reverse_file_index_1.get(self.startdownloadfile))
                for key in range(start_index, 61):
                    self.downloadfile.append(self.file_index_1.get(str(key)))            
        self.model = QtGui.QStandardItemModel(10,4)#儲存任意結構資料
        self.model.setHorizontalHeaderLabels(['    ','    ','    ','    '])

        self.tableView.setModel(self.model)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setVisible(False)
        self.header = self.tableView.horizontalHeader()       

        if int(len(self.downloadfile) % 4) == 0:
            rows = int(len(self.downloadfile)/4)
            self.outputedata = numpy.full((rows,4), numpy.nan,  dtype='object')
            self.outputedata.ravel()[:len(self.downloadfile)] = self.downloadfile     
       
        elif int(len(self.downloadfile) % 4) == 3:
            rows = int(len(self.downloadfile)/4)+1
            self.outputedata = numpy.full((rows,4), numpy.nan, dtype='object')
            self.outputedata.ravel()[:len(self.downloadfile)] = self.downloadfile

        elif int(len(self.downloadfile) % 4) == 2:
            rows = int(len(self.downloadfile)/4)+1
            self.outputedata = numpy.full((rows,4), numpy.nan, dtype='object')
            self.outputedata.ravel()[:len(self.downloadfile)] = self.downloadfile
        
        elif int(len(self.downloadfile) % 4) == 1:
            rows = int(len(self.downloadfile)/4)+1
            self.outputedata = numpy.full((rows,4), numpy.nan, dtype='object')
            self.outputedata.ravel()[:len(self.downloadfile)] = self.downloadfile
        
        
        myrows , mycols = self.outputedata.shape
        for row in range(myrows):
            for column in range(mycols):
                if str(self.outputedata[row][column]) == 'nan':
                    pass           
                else:
                    self.i = QtGui.QStandardItem(str(self.outputedata[row][column]))            
                    self.i.setCheckable(True)                    
                    self.i.setEditable(False)
                    self.model.setItem(row,column,self.i)
                    mydownload_file = str(self.outputedata[row][column])
                    self.label_5.setText(mydownload_file+'下載')
                    mydownload_path = self.filedownload_path_index.get(self.reverse_file_index_1.get(mydownload_file))
                    myvalue = self.mydata.currentDownLoadPath(mydownload_path, mydownload_file, self.bar_progress)
                    # print(myvalue)
                    if myvalue == True:
                        self.i.setCheckState(QtCore.Qt.Checked)
                    else:
                        pass                                
                self.header.setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)
                    

               


        
        self.label_5.setText('下載完成')
        self.progressBar.setValue(0)

class WorkThread(QThread):
    
    trigger = pyqtSignal( )

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
            self.trigger.emit( )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())