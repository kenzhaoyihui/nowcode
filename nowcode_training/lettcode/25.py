# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        
    def MergeSort(self, lists):
        count = 0
        if len(lists) <= 1:
            return lists
        num = len(lists)/2
        left = self.MergeSort(lists[:num])
        right = self.MergeSort(lists[num:])

        l, r = 0, 0
        result = []
            
        # write code here

        # Method1, not pass
        # count = 0
        # for i in range(0, len(data)):
        #     for j in range(i+1, len(data)):
        #         if data[i]>data[j]:
        #             count += 1
        # return count

        # Method2, Merge Sort


s = Solution()
a = [2,3,4,5,6,7,8,1,0]
print s.InversePairs(a)