#!/usr/bin/env/python3

__author__ = "kenzhaoyihui"

from xmlrpclib import ServerProxy

s = ServerProxy("http://127.0.0.1:8000")
s.hello()