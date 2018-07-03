# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n, k):
        # write code here
        # a = []
        # b = [str(x) for x in range(1, n+1)]
        # for x in range(0, len(b)):
        #     count = 0
        #     for j in range(0, len(b[x])):
        #         if b[x][j] == '1':
        #             count += 1
        #     a.append(count)

        # summ = 0
        # for i in a:
        #     summ += i
        # return summ

                # a = []
        # b = [str(x) for x in range(1, n+1)]
        # for x in range(0, len(b)):
        #     count = 0
        #     for j in range(0, len(b[x])):
        #         if b[x][j] == '1':
        #             count += 1
        #     a.append(count)

        # summ = 0
        # for i in a:
        #     summ += i
        # return summ

        res, tmp, base = 0, n, 1

        while tmp:
            last = tmp%10
            tmp = tmp/10
            res += base*tmp

            if last==k:
                res += n%base + 1
                
            elif last>k:
                res += base
            base *= 10
        return res

s = Solution()
print s.NumberOf1Between1AndN_Solution(2593, 5)