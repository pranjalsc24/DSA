#  middle of the linked list
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

    
        len_list=0
        start=node=head
        while start:
            len_list +=1
            start=start.next

        middle= len_list//2

        counter=0
        while node:
            if counter==middle:
                return node
            else:
                counter+=1
                node=node.next
        return None                



        