# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # result = False
        # if pRoot1 and pRoot2:
        #     if(pRoot1.val == pRoot2.val):
        #         result = self.IsSubtree(pRoot1, pRoot2)
        #     if not result:
        #         result = self.HasSubtree(pRoot1.left, pRoot2)
        #     if not result:
        #         result = self.HasSubtree(pRoot1.right, pRoot2)

        # return result

        if not pRoot1 or not pRoot2:
            return False
        return self.IsSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)


    def IsSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val!=pRoot2.val:
            return False
        if pRoot1.val == pRoot2.val:
            return self.IsSubtree(pRoot1.left, pRoot2.left) and self.IsSubtree(pRoot1.right, pRoot2.right)

s = Solution()
p = TreeNode(0)
p.left = TreeNode(2)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right.left = TreeNode(5)
p.right.right = TreeNode(6)

q = TreeNode(2)
q.left = TreeNode(5)
q.right = TreeNode(6)

print s.HasSubtree(p, q)