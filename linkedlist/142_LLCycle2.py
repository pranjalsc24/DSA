# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head==None or head.next==None:
#             return None
        
#         slow = head
#         fast = head
#         start = head

#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 while slow != start:
#                     slow = slow.next
#                     start = start.next
#                 return start
        
#         return None


# // https://www.youtube.com/watch?v=QfbOhn0WZ88&ab_channel=takeUforward

# /**
#  * Definition for singly-linked list.
#  * class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) {
#  *         val = x;
#  *         next = null;
#  *     }
#  * }
#  */
# public class Solution {
#     public ListNode detectCycle(ListNode head) {
#         if (head==null || head.next==null)
#             return null;
        
#         ListNode slow=head;
#         ListNode fast=head;
#         ListNode start=head;

#         while(fast.next!=null && fast.next.next!=null){
#             slow=slow.next;
#             fast=fast.next.next;

#             if(slow==fast){
#                 while(slow != start){
#                     slow=slow.next;
#                     start=start.next;
#                 }
#                 return start;
#             }
#         }
#         return null;
#         }
#   }


        