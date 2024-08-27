# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        node = head
        count = 1
        while node.next:
            count += 1
            node = node.next

        node = head
        if count - n == 0:
            head = head.next


        for i in range(1, count):
            if i == count-n:
                node.next = node.next.next
            else:
                node = node.next
        print(count)
        return head