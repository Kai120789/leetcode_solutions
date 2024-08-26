#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        count1 = ''
        while l1:
            count1 += str(l1.val)
            l1 = l1.next
        
        count2 = ''
        while l2:
            count2 += str(l2.val)
            l2 = l2.next

        count1 = count1[::-1]
        count2 = count2[::-1]

        summ = int(count1) + int(count2)
    

        print(summ)

        str_sum = str(summ)
        str_sum = str_sum[::-1]
        count = 0
        while count < len(str_sum):
            if count == 0:
                head = res = ListNode(int(str_sum[count]))
            else:
                res.next = ListNode(int(str_sum[count]))
                res = res.next
            count += 1


        return head