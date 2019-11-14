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
    import temperatures
except ImportError:
    print("temperature modules not found!")
    exit()

class MCpuTemp(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi()
        self.m_Temperature = temperatures.Temperature()

    def setupUi(self):
        # self.setObjectName("Monitor")
        self.setWindowTitle("Monitor")
        # 设置窗口自适应
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # self.resize(150, 50)
        # 设置窗口
        self.setWindowFlags(Qt.Qt.FramelessWindowHint # 去掉窗体边框
            | QtCore.Qt.Tool # 隐藏任务栏图标
            | QtCore.Qt.WindowStaysOnTopHint) # 窗口置顶
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
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        # 设置label颜色及固定大小
        self.label.setStyleSheet("background-color:rgb(0, 255, 255, 255);color:rgb(100, 0, 100, 255);border:0px;border-radius:4px")
        # self.label.setFixedSize(55, 40)

        # QTimer
        self.m_timer = QtCore.QTimer()
        self.m_timer.timeout.connect(self.timeOut)
        self.m_timer.start(200) # ms

        # 为label安装事件过滤器以实现拖拽 signal and slots
        self.label.installEventFilter(self)

    def timeOut(self):
        CpuTemp = self.m_Temperature.getCpuTemp()
        self.label.setText("CPU: " + str(CpuTemp) + "°C")
        # set color
        CpuTemp = 100
        colorVal = 100 - CpuTemp
        colorVal = 0 if colorVal < 0 else colorVal
        colorVal = 50 if colorVal > 50 else colorVal
        colorVal *= 2
        colorStr = "hsl(" + str(colorVal) + ", 255, 255, 255)"
        print(colorStr)
        self.label.setStyleSheet("background-color:" + colorStr + ";color:rgb(100, 0, 100, 255);border:0px;border-radius:4px")

def main():
    app = QApplication(sys.argv)
    w = MCpuTemp()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
