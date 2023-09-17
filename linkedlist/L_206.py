# REVERSE LINKED LIST

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
    #    ------optimal solution----------   time=o(n)  space=o(1) because we are only using pointers not any data structure to store the values
        # prev=None
        # curr=head
        # while curr:
        #     nxt=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=nxt
        # return prev 

    #   ---------using recursion---------  time=o(n) space=o(n)   in this we will use data structure to store the values

        if not head:
            return None
        newHead=head
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head
        head.next=None

        return newHead    


