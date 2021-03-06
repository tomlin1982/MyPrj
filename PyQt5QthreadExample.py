# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from QThread_Example_UI import Ui_Form

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 实例化线程对象
        self.work = WorkThread()
        self.runButton.clicked.connect(self.execute)

    def execute(self):
        # 启动线程
        self.work.start()
        # 线程自定义信号连接的槽函数
        self.work.trigger.connect(self.display)

    def display(self,str):
        # 由于自定义信号时自动传递一个字符串参数，所以在这个槽函数中要接受一个参数
        self.listWidget.addItem(str)

class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        #重写线程执行的run函数
        #触发自定义信号
        for i in range(20):
            time.sleep(1)
            # 通过自定义信号把待显示的字符串传递给槽函数
            self.trigger.emit(str(i))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())