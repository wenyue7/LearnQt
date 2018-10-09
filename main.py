# -*- coding: utf-8 -*-

import sys,os,datetime,time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

sys.path.append(os.getcwd())

import pyInterface,getInfo

def main():
	app = QApplication(sys.argv)
	Form = QMainWindow()
	w = pyInterface.Ui_MainWindow()
	w.setupUi(Form)
	Form.show()

        #不知道什么原因使用while循环总是崩溃,所以改用界面里的定时器
#        while(True):
#            Cpuinfo = getInfo.getCpuInfo()
#            Meminfo = getInfo.getMemInfo()
#            time.sleep(0.2)
#            w.setShowValue(Cpuinfo, Meminfo)

	exit(app.exec_())

if __name__ == '__main__':
	main()
