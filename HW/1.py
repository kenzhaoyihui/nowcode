#!/usr/bin/env python2.7

x = raw_input()

a = []
for i in x[::-1]:
    if i == ' ':
        break
    a.append(i)
print len(a)