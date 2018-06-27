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


def four():
    di = {"wang": 1, "li": 2}
    for index in di:
        print(di[index])

def five():
    octes = [192, 168, 0, 1]
    ss ='{:02d}---{:02d}---{:02d}---{:02d}'.format(*octes)
    print(ss)

def six():
    name = "123"
    print(name.isalnum())
    print("{0:x<8}".format(name))

if __name__ == '__main__':
    six()