// /**
//  * Definition for singly-linked list.
//  * public class ListNode {
//  *     int val;
//  *     ListNode next;
//  *     ListNode() {}
//  *     ListNode(int val) { this.val = val; }
//  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//  * }
//  */
// class Solution {
//     public ListNode deleteDuplicates(ListNode head) {
//         ListNode current=head;
//         if(head==null){
//           return head;
//         }
//          while(current.next!=null) {
//           if (current.next.val == current.val){
//             current.next=current.next.next;
//           }
//           else{
//             current=current.next;
//           }

//         }
//         return head;
//     }
// }


// ---------------------python--------------------------
// # Definition for singly-linked list.
// # class ListNode(object):
// #     def __init__(self, val=0, next=None):
// #         self.val = val
// #         self.next = next
// class Solution(object):
//     def deleteDuplicates(self, head):
//         """
//         :type head: ListNode
//         :rtype: ListNode
//         """
//         current=head
//         while (current and current.next):
//             if (current.next.val== current.val):
//                 current.next=current.next.next
//             else:
//                 current=current.next

//         return head            

            