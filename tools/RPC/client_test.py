#!/usr/bin/env/python3

__author__ = "kenzhaoyihui"

from xmlrpclib import ServerProxy

s = ServerProxy("http://127.0.0.1:8000")
s.hello()

s.pwd()
s.ls()
s.cp('client_test.py', 'client_test_copy1.py')
s.mkdir('tmp1')
s.show()