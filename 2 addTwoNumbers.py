#!/usr/bin/python3
# Author fengru
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headNode = ListNode(0)
        point = headNode
        sum = 0
        while (l1 != None) or (l2 != None) :
            if(l1 != None) :
                sum = sum + l1.val
                l1 = l1.next
            if(l2 != None) :
                sum = sum + l2.val
                l2 = l2.next
            newNode = ListNode(sum % 10)
            point.next = newNode
            point = point.next
            sum = sum//10
        if sum > 0 :
            newNode = ListNode(sum)
            point.next = newNode
        return headNode.next
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
print(l3.val)
print(l3.next.val)
print(l3.next.next.val)
