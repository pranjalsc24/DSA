# lonest subarray with sum=k

# import java. lang. Math. *;
# public class Solution {
#     public static int longestSubarrayWithSumK(int []a, long k) {
#         // Write your code here
#         int len=0;
#         for(int i=0;i<a.length;i++){
#             int sum=0;
#             for(int j=i;j<a.length;j++){
#                 sum+=a[j];
#                 if(sum==k){
#                   len=Math.max(len, j-i+1);
#                 }
#             }
#         }
#         return len;

#     }
# }

