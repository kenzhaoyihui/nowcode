#!/usr/bin/env python2.7

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # min = rotateArray[0]
        # for i in range(1, len(rotateArray)):
        #     if rotateArray[i] <= min:
        #         min = rotateArray[i]
        # return min

        return sorted(rotateArray)[0]