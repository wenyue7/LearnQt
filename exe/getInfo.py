# -*- coding: utf-8 -*-
# 如果想写中文注释需要加上上边这句
# 先下载psutil库:pip install psutil
import os,datetime,time
import psutil

def getCpuInfo():
    cpu = "%0.2f" %psutil.cpu_percent(interval=1) + "%"
    return cpu

def getMemInfo():
    data = psutil.virtual_memory()
    total = data.total  #总内存,单位为byte
    free = data.available #可用内存
    memory = "%d" %(int(round(data.percent))) + "%"
    return memory

def main():
    while(True):
        Cpuinfo = "CPU: " + getCpuInfo()
        Meminfo = "Mem: " + getMemInfo()
        time.sleep(0.2)
        count = 14 - len(Cpuinfo)
        space = " "
        for i in range(count):
            space += " "
            count = count - 1
        print (Cpuinfo, space, Meminfo)

if __name__ == "__main__":
    main()
	
