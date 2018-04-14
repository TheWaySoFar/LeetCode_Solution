#/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei = 0
        head, p, p1 = None, None, None
        while l1 != None or l2 != None or jinwei != 0:
            l1val, l2val = 0, 0
            if l1 != None:
                l1val = l1.val
                l1 = l1.next
            if l2 != None:
                l2val = l2.val
                l2 = l2.next
            x = l1val + l2val + jinwei
            jinwei = x // 10
            x = x % 10
            p1 = ListNode(x)
            if p == None:
                p = p1
            else:
                p.next = p1
                p = p1
            if head == None:
                head = p
        return head

def printList(l):
    if l == None:
        return
    printList(l.next)
    print("%d" % l.val, end='')

def createList(a):
    head, p, p1 = None, None, None
    for x in a:
        p1 = ListNode(x)
        if p == None:
            p = p1
        else:
            p.next = p1
            p = p1
        if head == None:
            head = p
    return head

if __name__ == '__main__':
    l1 = createList([2, 4, 3])
    l2 = createList([5, 6, 7])
    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    printList(l3)


