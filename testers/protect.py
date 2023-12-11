#!/usr/bin/python3

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        
        from attribute_tests import A
        x = A()
        x.pub

        x.pub = x.pub + " and my value can be changed"
        x.pub
