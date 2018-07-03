# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)

s = Solution()
p = TreeNode(0)
p.left = TreeNode(1)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right.left = TreeNode(5)
p.right.right = TreeNode(6)

s.Mirror(p)
