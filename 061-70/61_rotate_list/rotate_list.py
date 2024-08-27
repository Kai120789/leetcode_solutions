# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        count = 0
        node = head
        while node.next:
            node = node.next
            count += 1

        num = k % (count + 1)

        for j in range(0, num):

            node = head
            cnt = 0
            while cnt < count + 1:
                node = node.next
                cnt += 1
                if cnt == count:
                    node.next = head
                    head = node
                    for i in range(0, count):
                        node = node.next
                        if i == count - 1:
                            node.next = None


        print(count)
        return head