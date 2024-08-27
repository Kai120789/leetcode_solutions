# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if(head == None or head.next == None):
            return  head

        first = head
        while head.next:
            if (head.val == head.next.val):
                head.next = head.next.next
            else:
                head = head.next
        return first
