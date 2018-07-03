# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        set_num = set(numbers)
        dict1 = {}
        for i in set_num:
            count = 0
            for j in numbers:
                if j == i:
                    count += 1
            dict1[i] = count

        if sorted(dict1.items(), key=lambda d: d[1])[-1][1]>len(numbers)/2:
            return sorted(dict1.items(), key=lambda d: d[1])[-1][0]
        else:
            return 0

s = Solution()
a = [1,2,3,2,4,2,5,4,2]
print s.MoreThanHalfNum_Solution(a)