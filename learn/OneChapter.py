# -*- utf-8 -*-
import datetime
import time

import psutil
import serial.tools.list_ports as ts


def str_practise():
    print(3 + 2 < 5 - 7)
    print(7 / 4)
    name_result = 70 / 4.0
    list_result = ['name', 'wang', 'hello']

    print("foo %s bar %s coffee" % ("blah", "asdf"))
    print(name_result)

    # %只能用于字符串 列表 元组
    print("ok %s" % "name" + str(len(list_result)))

    hilarious = True

    print("hello world ! '%s'" % 'wpy')

    time_result = time.strftime('%Y-%m-%d %H:%M:%S')
    print(time_result)


def cpu_info():
    cpu_result = psutil.cpu_times()
    print(cpu_result)
    memory_view = psutil.virtual_memory()
    print(memory_view)
    swap_result = psutil.swap_memory()
    print(swap_result.total)
    print(swap_result.total / (1024 * 1024 * 1024))
    print('开机时间', datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S"))

    psutil.net_io_counters()
    print(psutil.users())

    #     查看所有进程的状态
    print(psutil.pids())


def serial_info():
    # 获取所有串口信息
    port_list = list(ts.comports())
    print(len(port_list))


if __name__ == '__main__':
    # cpu_info()
    serial_info()
