# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        a = []
        b = []
        for s in array:
            if s%2==1:
                a.append(s)
            else:
                b.append(s)
        return a+b