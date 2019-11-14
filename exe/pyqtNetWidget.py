# -*- coding: utf-8 -*-

try:
    import sys,os
    from PyQt5 import Qt, QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
except ImportError:
    print('some modules not found!')
    exit()

sys.path.append(os.getcwd())
try:
    import netinfo
except ImportError:
    print('netinfo module not found!')
    exit()

class NetTraffic(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.m_netTraffic = netinfo.NetTraffic()

    def setupUi(self):
        self.setWindowTitle("NetTraffic")
        # 设置窗口自适应
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.gridLayout.setSpacing(0)  #消除内部组件之间的缝隙
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  #消除组件的边缘
        self.label = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        # 设置label颜色及固定大小
        self.label.setStyleSheet("background-color:rgb(0, 155, 155, 255);color:rgb(255, 255, 255, 255);border:0px")
        self.label_2.setStyleSheet("background-color:rgb(0, 100, 100, 255);color:rgb(255, 255, 255, 255);border:0px")

        # QTimer
        self.m_timer = QtCore.QTimer()
        self.m_timer.timeout.connect(self.timeOut)
        self.m_timer.start(200) # ms

    def timeOut(self):
        key_info, net_in, net_out, net_inSum, net_outSum = self.m_netTraffic.getRate()
        if(int(net_inSum) > 1024):
            net_inSum = float("%0.2f" % (net_inSum/1024))
            download = "%-1s%s %s" % ("↓", str(net_inSum), "MB/s")
        else:
            download = "%-1s%s %s" % ("↓", str(net_inSum), "KB/s")
        if(int(net_outSum) > 1024):
            net_outSum = float("%0.2f" % (net_outSum/1024))
            upload = "%-1s%s %s" % ("↑", str(net_outSum), "MB/s")
        else:
            upload = "%-1s%s %s" % ("↑", str(net_outSum), "KB/s")
        self.label.setText(download)
        self.label_2.setText(upload)

def main():
    app = QApplication(sys.argv)
    w = NetTraffic()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
