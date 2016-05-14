from abc import ABCMeta, abstractmethod

class AB(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def speak(self):
        print "spoken"

    @abstractmethod
    def shout(self, less):
        print "shouted"

class DEF(AB):
    def speak(self):
        super(DEF, self).speak()
        print "inherited"


obj = DEF()
print obj.speak()
