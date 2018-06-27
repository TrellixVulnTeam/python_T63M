# -*- utf-8 -*-
import threading


def one_t():
    tuple_one = ("wang", 1, 2, 3)
    tuple_two = ("li", 22, "liang")

    tuple_three = tuple_one + tuple_two
    print(tuple_three)


class Student:
    '''重要的:------------->>>类和实例'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(self.name, self.age)


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def hello(self):
        print("hello")

if __name__ == "__main__":
    Student("wang", 123).hello()
    Singleton().hello()