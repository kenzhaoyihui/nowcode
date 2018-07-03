#/usr/bin/env python3

__author__ = "kenzhaoyihui"

import os
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn

def pwd():
    return os.getcwd()

def ls(directory=None):
    if directory is None:
        directory = pwd()
    try:
        return os.listdir(directory)
    except OSError as e:
        return e

def cd(directory):
    try:
        os.chdir(directory)
    except OSError as e:
        return e

    return 'change current working directory to: %s' % (directory)

def mkdir(directory):
    try:
        os.mkdir(directory)
    except OSError as e:
        return e
    else:
        return 'successfully create directory: %s' % directory

def cp(src, dest):
    with open(src, 'r') as fin:
        with open(dest, 'w') as fout:
            fout.write(fin.read())
    return 'copy %s-> %s' % (src, dest)

def hello():
    print "helloworld!"

class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def show(self):
        return str(self)

    def __str__(self):
        return 'Person(name=%s, age=%s)' % (self._name, self._age)
#s = SimpleXMLRPCServer(('', 8000), allow_none=True)

s = ThreadXMLRPCServer(('', 8000), allow_none=True)

s.register_function(pwd) # register function
s.register_function(ls)
s.register_function(cd)
s.register_function(mkdir)
s.register_function(cp)
s.register_function(hello)

p = Person('python', 20)
s.register_instance(p)

s.serve_forever()
