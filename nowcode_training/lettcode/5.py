#!/usr/bin/env python2.7

class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    # Method2
    # def pop(self):
    #     if self.stack2 == []:
    #         while self.stack1:
    #             self.stack2.append(self.stack1.pop())
    #         return self.stack2.pop()
    #     return self.stack2.pop()

    # Method1
    # def pop(self):
    #     while self.stack1:
    #         self.stack2.append(self.stack1.pop())
    #     val = self.stack2.pop()
    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())
    #     return val

    # def push(self, node):
    #     if self.stack1 == []:
    #         while self.stack2:
    #             self.stack1.append(self.stack2.pop())
    #     self.stack1.append(node)

    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print s.pop()
s.push(5)
print s.pop()