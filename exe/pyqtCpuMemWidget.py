# -*- coding: utf-8 -*-

try:
    import sys,os
    from PyQt5 import Qt, QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
except ImportError:
    print("some modules not found!")
    exit()

sys.path.append(os.getcwd())
try:
    import cpumeminfo
except ImportError:
    print("cpumeminfo modules not found!")
    exit()

class MonitorCPUMem(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi()
        self.m_CpuMemInfo = cpumeminfo.CpuMemInfo()

    def setupUi(self):
        # self.setObjectName("Monitor")
        self.setWindowTitle("Monitor")
        # 设置窗口为固定值
        # self.setFixedSize(90, 30)
        # 设置窗口自适应
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        # 设置背景透明
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        # 去掉缝隙
        self.setContentsMargins(0, 0, 0, 0)
        # 移动窗口
        self.move(1000, 600)
        
        # 添加组件
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(0)  #消除内部组件之间的缝隙
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  #消除组件的边缘
        self.label = QtWidgets.QLabel(self)
        # self.label.setText("")
        # self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        # self.label_2.setText("")
        # self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        # 设置label颜色及固定大小
        self.label.setStyleSheet("background-color:rgb(0, 255, 255, 255);color:rgb(255, 0, 255, 255);border:0px;border-radius:6px")
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 0, 255);color:rgb(255, 0, 255, 255);border:0px;border-radius:6px")

        # QTimer
        self.m_timer = QtCore.QTimer()
        self.m_timer.timeout.connect(self.timeOut)
        self.m_timer.start(200) # ms

    def setDisValue(self, CPUValue, MemValue):
        self.label.setText(CPUValue)
        self.label_2.setText(MemValue)

    def timeOut(self):
        Cpuinfo = "CPU\n " + self.m_CpuMemInfo.getCpuInfo() + "%"
        Meminfo = "Mem\n " + self.m_CpuMemInfo.getMemInfo() + "%"
        self.label.setText(Cpuinfo)
        self.label_2.setText(Meminfo)

def main():
    app = QApplication(sys.argv)
    w = MonitorCPUMem()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
