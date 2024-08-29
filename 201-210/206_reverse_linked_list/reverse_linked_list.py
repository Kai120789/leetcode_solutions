# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        count = 0

        if not head or not head.next:
            return head

        while node1.next:
            node1 = node1.next
            count += 1
        last = node1
        node1.next = head


        # [5, 4, 1, 2, 3]
        flag = False
        for i in range(0, count):
            if flag:
                node2 = last.next #4
                node1 = last.next #4
                
                for l in range(0, i - 1):
                    node1 = node1.next

            for j in range(0, count - 1):
                node2 = node2.next #3
            
            node2.next = head # 3 - 1
            node1.next = node2 # 4 - 3
            print(1)

            # [5, 4, 3, 1, 2]
            for k in range(0, count - 1 - i):
                node2 = node2.next 
            node2.next = None

            flag = True

        return last