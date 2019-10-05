# -*- coding: utf-8 -*-

import sys,os
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

sys.path.append(os.getcwd())
import getInfo

class MonitorCPUMem(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # self.setObjectName("Monitor")
        self.setWindowTitle("Monitor")
        # 设置窗口为固定值
        self.setFixedSize(120, 50)
        # self.resize(150, 50)
        # 设置窗口
        self.setWindowFlags(Qt.Qt.FramelessWindowHint # 去掉窗体边框
            # | QtCore.Qt.WindowMinimizeButtonHint # 使能最小化按钮
            # | QtCore.Qt.WindowMaximizeButtonHint # 使能最大化按钮
            # | QtCore.Qt.WindowCloseButtonHint # 使能关闭按钮
            # | QtCore.Qt.WindowSystemMenuHint # 不知道有啥用
            | QtCore.Qt.Tool # 隐藏任务栏图标
            | QtCore.Qt.WindowStaysOnTopHint) # 窗口置顶
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # 去掉窗口边界  未奏效
        self.setStyleSheet("border:0px")
        # 设置背景透明
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        # 去掉缝隙
        self.setContentsMargins(0, 0, 0, 0)
        # self.setContentsMargins(0)
        # 移动窗口
        self.move(1000, 600)
        
        # 添加组件
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(0)  #消除添加组件之间的缝隙
        # self.gridLayout.setMargin(0)
        self.label = QtWidgets.QLabel(self)
        # self.label.setText("")
        # self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        # self.label_2.setText("")
        # self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        # 设置label颜色及固定大小
        self.label.setStyleSheet("background-color:rgb(0, 255, 255, 255);color:rgb(255, 0, 255, 255);border:0px")
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 0, 255);color:rgb(255, 0, 255, 255);border:0px")
        self.label.setFixedSize(80, 40)
        self.label_2.setFixedSize(40, 40)

        # QTimer
        self.m_timer = QtCore.QTimer()
        self.m_timer.timeout.connect(self.timeOut)
        self.m_timer.start(200) # ms

        # 为label安装事件过滤器以实现拖拽 signal and slots
        self.label.installEventFilter(self)
        self.label_2.installEventFilter(self)

    def setDisValue(self, CPUValue, MemValue):
        self.label.setText(CPUValue)
        self.label_2.setText(MemValue)

    def timeOut(self):
        Cpuinfo = "CPU\n " + getInfo.getCpuInfo()
        Meminfo = "Mem\n " + getInfo.getMemInfo()
        self.label.setText(Cpuinfo)
        self.label_2.setText(Meminfo)

# 以下事件函数未必在本程序中用到,放在这里只是作为学习
    def event(self, event):
        # print("this is event fun")
        return super().event(event)

    def eventFilter(self, watched, event):
        if ((watched == self.label) or (watched == self.label_2)) :
            if  event.type() == Qt.QEvent.MouseButtonPress :
                # self.__mousePressPos = event.globalPos()
                self.__mouseMovePos = event.globalPos()
                return True
            return False
        else:
            return super().eventFilter(watched, event)

    def mousePressEvent(self, event):
        pass

    # 1. 相对位置：每个Qwidget都能通过pos()获取到相对自己父类窗口的位置
    # 2. 绝对位置：pWidget->mapToGlobal(QPoint(0,0)) ;将当前控件的相对位置转换为屏幕绝对位置
    # 3. 绝对位置转为相对位置： pWidget->mapFromGlobal(QPoint(0,0)), 将绝对位置对应到控件的相对位置
    def mouseMoveEvent(self, event):
        currPos = self.mapToGlobal(self.pos())
        diff = event.globalPos() - self.__mouseMovePos
        newPos = self.mapFromGlobal(currPos + diff)
        self.move(newPos)
        self.__mouseMovePos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
        	self.m_timer.stop()
        	self.close()

def main():
    app = QApplication(sys.argv)
    w = MonitorCPUMem()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()