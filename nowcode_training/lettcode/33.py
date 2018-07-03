# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        if index == 1:
            return 1
        t2, t3, t5 = 0, 0, 0
        res = [1]
        for i in range(1, index):
            res.append(min(res[t2]*2, res[t3]*3, res[t5]*5))
            if res[i] == res[t2]*2:
                t2 += 1
            if res[i] == res[t3]*3:
                t3 += 1
            if res[i] == res[t5]*5:
                t5 += 1
        return res[index-1]



s = Solution()
print s.GetUglyNumber_Solution(5)