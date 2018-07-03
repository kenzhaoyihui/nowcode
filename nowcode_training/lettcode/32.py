# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        # num = map(str, numbers)
        # array = sorted(num, cmp=lambda x, y: cmp(x+y, y+x))
        # return ''.join(array)

        lamb = lambda n1, n2: cmp(str(n1)+str(n2), str(n2)+str(n1))
        array = sorted(numbers, cmp=lamb)
        print array
        return ''.join([str(i) for i in array])

s = Solution()
a = [3, 32, 321]
print s.PrintMinNumber(a)