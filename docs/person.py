# -*- coding: utf-8 -*-

class Person(object):
    "Person"

    def __init__(self, name):
        """
        :param name: set your name.
        """
        self.name = name

    def greeting(self):
        """
        :retval: greeting message.
        """
        return "My name is {}".format(self.name)

