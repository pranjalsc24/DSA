// // https://www.youtube.com/watch?v=nhEMDKMB44g&t=801s&ab_channel=takeUforward
// import java.util.*;


// class Solution {
//     public int findMin(int[] nums) {
//         int low=0, high=nums.length-1;
//         int ans=Integer.MAX_VALUE;

//         while(low<=high){
//             int mid=low+(high-low)/2;

//             if(nums[low]<=nums[mid]){
//                 ans= Math.min(ans,nums[low]);
//                 low=mid+1;
//             }
//             else{
//                 high=mid-1;
//                 ans= Math.min(ans,nums[mid]);
//             }
//         }
//         return ans;
//     }
// }