# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        targets = []
        while node.next:
            if node.val == node.next.val and node.val not in targets:
                targets.append(node.val)

            node = node.next

        print(targets)

        node = head

        while node.next:
            if node.next.val in targets:
                node.next = node.next.next
            else:
                node = node.next

        return head if head.val not in targets else head.next