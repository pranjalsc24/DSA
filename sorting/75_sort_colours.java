// class Solution {
//     public void sortColors(int[] nums) {
//         int cnt0=0;
//         int cnt1=0;
//         int cnt2=0;

//         for(int i=0;i<nums.length;i++){
//             if (nums[i]==0){
//              cnt0++;
//             } 
//             else if (nums[i]==1){
//              cnt1++;
//             } 
//             else{
//                 cnt2++;
//             }
//         }
//         for(int i=0;i<cnt0;i++){
//             nums[i]=0;
//         }
//         for(int i=cnt0;i<cnt0+cnt1;i++){
//             nums[i]=1;
//         }
//          for(int i=cnt0+cnt1;i<nums.length;i++){
//             nums[i]=2;
//         }

        
//     }
// }


// // class Solution {
// //     public void sortColors(int[] nums) {

// //         int i = 0;
// //         int j = nums.length - 1;
// //         int k = 0;

// //         while (k <= j) {
// //             if (nums[k] == 0) {
// //                 int temp = nums[i];
// //                 nums[i] = nums[k];
// //                 nums[k] = temp;
// //                 i++;
// //                 k++;
// //             } else if (nums[k] == 2) {
// //                 int temp = nums[j];
// //                 nums[j] = nums[k];
// //                 nums[k] = temp;
// //                 j--;
// //             } else {
// //                 k++;
// //             }
// //         }
        
// //     }
// // }