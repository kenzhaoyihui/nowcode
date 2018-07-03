# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # while n<=39:
        #     if n==0:
        #         return 0
        #     if n==1 or n==2:
        #         return 1
        #     if n > 2:
        #         return self.Fibonacci(n-1) + self.Fibonacci(n-2)

        while n<=39:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n>=3:
                s = []
                s.append(1)
                s.append(1)
                for i in range(2, n):
                    s.append(s[i-1]+s[i-2])
                return s[n-1]

x = input("number: ")
s = Solution()
print s.Fibonacci(x)