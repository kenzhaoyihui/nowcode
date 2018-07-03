#!/usr/bin/env python2.7

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        
        return root