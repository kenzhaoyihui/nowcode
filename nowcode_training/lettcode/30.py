# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # a = []
        # for i in range(1,len(array)+1):
        #     sum = 0
        #     for j in array[:i]:
        #         sum += j
        #     a.append(sum)
        
        # max1 = a[0]
        # for x in a:
        #     if x>max1:
        #         max1 = x
        # return max1

        #Method1
        # maxn, summ = 0, 0
        # for i in array:
        #     if summ <=0:
        #         summ = i
        #     else:
        #         summ += i
        #     if summ>maxn:
        #         maxn = summ
        # return maxn

        #Methdo2
        lst = []
        for i in range(0, len(array)):
            maxn = array[i]
            lst.append(maxn)
            for j in range(i+1, len(array)):
                maxn += array[j]
                lst.append(maxn)
        return sorted(lst)[-1]



s = Solution()
print s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
print s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])