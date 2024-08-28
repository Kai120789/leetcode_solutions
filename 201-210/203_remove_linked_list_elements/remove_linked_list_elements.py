# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        while node.next:
            if node.next.val == val:
                if not node.next.next:
                    node.next = None
                else:
                    node.next = node.next.next
            else:
                node = node.next

        if head.val == val:
            head.val = ""
            if head.next:
                head = head.next

        return head