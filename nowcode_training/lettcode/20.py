# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._list = []

    def push(self, node):
        # write code here
        self._list.append(node)
    def pop(self):
        # write code here
        self._list.pop()
    def top(self):
        # write code here
        self._list.pop()
    def min(self):
        # write code here
        if self._list != []:
            minn = self._list[0]
            for i in self._list:
                if i<=minn:
                    minn = i
            return minn
