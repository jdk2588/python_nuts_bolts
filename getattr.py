#!/usr/bin/python
# Author <Jaideep Khandelwal jdk2588@gmail.com>
class A(object):
    def __init__(self):
      print "In Init"
      self.a = 50

    def __getattr__(self, attr):
        if attr in ["b"]:
            return 42
        elif attr in ["c"]:
            return 89

        raise AttributeError("%r object has no attribute %r" % (self.__class__, attr))

class Proxy(object):
    def __get__(self, instance, type=None, *args, **kwargs):
        return A()

class C(object):
    tran = Proxy()

class D(C):
    def sample(self):
        x = self.tran
        y = self.tran
        z = self.tran
        print id(x)
        print id(y)
        print id(z)

d = D()
d.sample()
