# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here

        #Method1
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # else:
        #     return self.jumpFloor(number-1) + self.jumpFloor(number-2)

        #Method2
        # a = 1
        # b = 1
        # for i in range(number):
        #     a, b = b, a+b
        # return a

        if number == 1:
            return 1
        if number == 2:
            return 2
        else:
            a = []
            a.append(1)
            a.append(2)
            for i in range(2, number):
                a.append(a[i-2]+a[i-1])
        return a[number-1]

x = input("number: ")
s = Solution()
print s.jumpFloor(x)
