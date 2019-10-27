#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 程序来源:
# http://www.py3study.com/Article/details/id/347.html

try:
    import psutil
except ImportError:
    print('Error: psutil module not found!')
    exit()


def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}
    recvSum = {}
    sentSum = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)
    recvSum = psutil.net_io_counters().bytes_recv
    sentSum = psutil.net_io_counters().bytes_sent

    return key_info, recv, sent, recvSum, sentSum


def get_rate(func):

    import time

    key_info, old_recv, old_sent, old_recvSum, old_sentSum = func()

    time.sleep(1)

    key_info, now_recv, now_sent, now_recvSum, now_sentSum = func()

    net_in = {}
    net_out = {}
    net_inSum = {}
    net_outSum = {}


    for key in key_info:
        # float('%.2f' % a)
        net_in.setdefault(key, float('%.2f' %((now_recv.get(key) - old_recv.get(key)) / 1024)))
        net_out.setdefault(key, float('%.2f' %((now_sent.get(key) - old_sent.get(key)) / 1024)))
    net_inSum = float('%.2f' %((now_recvSum - old_recvSum) / 1024))
    net_outSum = float('%.2f' %((now_sentSum - old_sentSum) / 1024))

    return key_info, net_in, net_out, net_inSum, net_outSum


def main():
    while 1:
        try:
            key_info, net_in, net_out, net_inSum, net_outSum = get_rate(get_key)
            for key in key_info:
            # lo 是linux的本机回环网卡，以太网是我win10系统的网卡名
                if key != 'lo' or key == '以太网':
                    print("%-9sInput:\t %-5sKB/s\tOutput:\t %-5sKB/s" % (key+":", net_in.get(key), net_out.get(key)))
            print("%-9sInput:\t %-5sKB/s\tOutput:\t %-5sKB/s" % ("==>All:", net_inSum, net_outSum))
        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    main()