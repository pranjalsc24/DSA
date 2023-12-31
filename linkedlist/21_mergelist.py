#  Merge Two Sorted Lists
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head=ListNode()
        current=head

        while list1 and list2:
            if list1.val< list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next    

        if(list1!=None):
            current.next=list1
        else:
            current.next=list2

        return head.next 



# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;a
#  *     ListNode next;
#  *     ListNode() {}
#  *     ListNode(int val) { this.val = val; }
#  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
#  * }
#  */
# class Solution {
#     public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
#         ListNode head = new ListNode();
#         ListNode current = head;

#         while (list1 != null && list2 != null) {
#             if (list1.val < list2.val) {
#                 current.next = list1;
#                 list1 = list1.next;
#             } else {
#                 current.next = list2;
#                 list2 = list2.next;
#             }
#             current = current.next;
#         }

#         if (list1 != null) {
#             current.next = list1;
#         } else {
#             current.next = list2;
#         }

#         return head.next;
        
#     }
# }           




        