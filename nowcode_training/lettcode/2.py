#!/usr/bin/env python

def replaceSpace(s):
    a = []
    for i in s:
        if i == ' ':
            i = '%20'
        a.append(i)
    return ''.join(a)




s = "We are happy"
print replaceSpace(s)