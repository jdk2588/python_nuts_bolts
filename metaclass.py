#!/usr/bin/python
# Author <Jaideep Khandelwal jdk2588@gmail.com>


class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)


class Temperature(object):
    celsius = Celsius()

t = Temperature()
print t.celsius
