# -*- utf-8 -*-
import datetime


def t1():
    now = datetime.datetime.now()
    now_str = now.strftime('%Y%m%d %H:%M:%S')
    print(now_str)
    now = now - datetime.timedelta(days=now.isoweekday())
    print(now)


if __name__ == '__main__':
    t1()
