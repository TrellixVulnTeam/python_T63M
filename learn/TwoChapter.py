# -*- coding=utf-8 -*-
from sys import argv


def one():
    print('请输入数字或者字母')
    a = input("name? ")
    print(a)

    print(argv)
    print(argv)
    print(argv)
    print(argv)
    print(argv)


def two():
    print("-".join("wang"))
    w1 = ["wang", "pei", "yuan"]
    w1 = "-".join(w1)
    print(w1)


def three():
    wa = ["wang", "li", "23", 45]
    wa[1] = 40
    for index in range(len(wa)):
        print(wa[index])
    ww = wa.pop()
    print(ww)


if __name__ == '__main__':
    three()
