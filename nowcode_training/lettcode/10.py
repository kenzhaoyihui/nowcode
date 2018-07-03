# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        else:
            a = []
            a.append(1)
            a.append(2)
            for i in range(2, number):
                a.append(a[i-2]+a[i-1])
        return a[number-1]
