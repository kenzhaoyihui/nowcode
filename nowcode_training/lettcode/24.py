# -*- coding:utf-8 -*-
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def FindPath(self, root, expectNumber):
    #     # write code here
    #     if root is None:
    #         return []
    #     if root and not root.left and not root.right and root.val == expectNumber:
    #         return [[root.val]]

    #     res = [] 
    #     left = self.FindPath(root.left, expectNumber-root.val)
    #     right = self.FindPath(root.right, expectNumber-root.val)
    #     for i in left+right:
    #         res.append([root.val]+i)
    #     return res

    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        rest = expectNumber
        pathlist = []
        path = []
        self.findallpath(root, rest, pathlist, path)
        return pathlist

    def findallpath(self, root, rest, pathlist, path):
        if root is None:
            return
        path.append(root.val)
        rest -= root.val

        if root.left is None and root.right is None:
            if rest == 0:
                #pathlist.append(path)
                pathlist.append(copy.deepcopy(path))
                #pathlist.append(copy.copy(path))
        self.findallpath(root.left, rest, pathlist, path)
        self.findallpath(root.right, rest, pathlist, path)

        path.pop()


s = Solution()
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right.left = TreeNode(3)
p.right.right = TreeNode(7)

print s.FindPath(p, 7)