// // kunal-linked list cycle concept
// class Solution {
//     public boolean isHappy(int n) {
//        int slow = n;
//        int fast = n;

//         do {
//             slow = findSquare(slow);
//             fast = findSquare(findSquare(fast));
//         } while (slow != fast);

//         if (slow == 1) {
//             return true;
//         }
//         return false;
//     }
//     private int findSquare(int number) {
//         int ans = 0;
//         while (number > 0) {
//             int rem = number % 10 ;
//             ans += rem * rem;
//             number /= 10;
//         }
//         return ans; 
//     }
// }


// class Solution(object):
//     def isHappy(self, n):
//         """
//         :type n: int
//         :rtype: bool
//         """
//         res=0
//         while(n>0):
//             i=n%10
//             res=res+ i*i
//             n=n/10
            
//         if(res==1):
//             return True

//         elif (res>6):
//             return self.isHappy(res)

//         else:
//             return False        
            
    