#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return newHead

# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         # write code here
#         if pHead == None or pHead.next == None:
#             return pHead
#         p1 = pHead
#         p2 = pHead.next
#         r = None
#         while p2:
#             r = p2.next
#             p2.next = p1
#             p1 = p2
#             p2 = r
#         pHead.next = None
#         return p1
            
        # l = []
        # while pHead:
        #     l.insert(0,pHead)
        #     pHead = pHead.next

        # newHead = ListNode(0)
        # tmp = newHead
        # for i in l:
        #     tmp.next = ListNode(i)
        #     tmp = tmp.next
        # return newHead.next
            
            
s = Solution()
p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)

print s.ReverseList(p)

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def ReverseList(self, pHead):
#         # write code here
#         if not pHead or not pHead.next:
#             return pHead
         
#         last = None
         
#         while pHead:
#             tmp = pHead.next
#             pHead.next = last
#             last = pHead
#             pHead = tmp
#         return last


