#!/usr/bin/env python2.7

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):

    def printListFormTailToHead(self, listNode):
        a = []
        head = listNode
        while head:
            a.insert(0, head.data)
            head = head.next
        return a