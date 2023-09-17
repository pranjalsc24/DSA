# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse(head):
            next = current = head
            prev = None 
            while current!=None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        head = ListNode()
        current = head
        carry = 0
        l1 = reverse(l1)
        l2 = reverse(l2)
        while (l1 != None or l2 != None or carry != 0):
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            carry = total // 10
            # Move list pointers forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        ans = reverse(head.next)
        return ans
        # return head.next
       

        

