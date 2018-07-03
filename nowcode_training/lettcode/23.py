# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        if len(sequence)==1:
            return True
        root = sequence[-1]

        i = 0
        while sequence[i]< root:
            i += 1
        k = i

        for j in range(k, len(sequence)-1):
            if sequence[j] < root:
                return False

        left_s = sequence[:k]
        right_s = sequence[k: len(sequence)-1]

        leftIs, rightIs = True, True
        if len(left_s):
            leftIs = self.VerifySquenceOfBST(left_s)
        if len(right_s):
            rightIs = self.VerifySquenceOfBST(right_s)
        return leftIs and rightIs

s = Solution()
print s.VerifySquenceOfBST([7,2,3,1,4,8,6,5])
