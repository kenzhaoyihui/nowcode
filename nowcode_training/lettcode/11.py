# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # count = 0
        # if n>=0:
        #     s = bin(n)
        # else:
        #     a = []
        #     n = abs(n)
        #     s = '1'+bin(n)[2:]
        #     for i in range(32-len(s)+1):
        #         s = '0'+s
        #     for i in s:
        #         if i=='1':
        #             i = '0'
        #         else:
        #             i = '1'
        #         a.append(i)
        #     s = ''.join(a)
        #     print s
        #     s = bin(int(s, 2)+1)
        
        # for i in s:
        #     if i == '1':
        #         count += 1
        # return count
        return sum([(n>>i & 1) for i in range(0,32)])


s = Solution()
print s.NumberOf1(-2147483648)


