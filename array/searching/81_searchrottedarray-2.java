// // https://www.youtube.com/watch?v=w2G2W8l__pc&ab_channel=takeUforward

// class Solution {
//     public boolean search(int[] nums, int target) {
        

//         int left = 0;
//         int right = nums.length - 1;
        
//         while (left <= right) {
//             int middle = (left+right)/ 2;
//             System.out.println(middle);
            
//             if (nums[middle] == target) return true;

//             // ----following codition for duplicates-----------
//             if(nums[left]==nums[middle] && nums[middle]==nums[right]){
//                 left=left+1;
//                 right=right-1;
//                 continue;

//             }
               
            
            
//             // ---left sorted----
//             if (nums[middle] >= nums[left]) {
//                 if (nums[left] <= target && target < nums[middle]) {
//                     right = middle - 1;
//                 } 
//                 else {
//                     left = middle + 1;
//                 }
//             } 
//             // ---right sorted---
//             else {
//                 if (nums[right] >= target &&  target > nums[middle]  ) {
//                     left = middle + 1;
//                 } else {
//                     right = middle - 1;
//                 }
//             }
//         }
        
//         return false;
//     }
// }