# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        # write code here
        A = []
        result = []
        if root is None:
            return False
        A.append(root)
        while A:
            curr = A.pop(0)
            result.append(curr.val)
            if curr.left:
                A.append(curr.left)
            if curr.right:
                A.append(curr.right)
        return result