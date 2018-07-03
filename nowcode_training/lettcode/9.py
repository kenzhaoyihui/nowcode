#!/usr/bin/env python2.7

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        else:
            return 2*self.jumpFloorII(number-1)