// // striver 

// import java.util.*;

// class Solution {
//     public int removeDuplicates(int[] nums) {
//         // ----below is optimal----

//         int i=0;
//         int n=nums.length;

//         for(int j=1; j<n; j++){
//             if(nums[j]!=nums[i]){
//                 nums[i+1]=nums[j];
//                 i++;
//             }
//         }
//         return i+1;


// //    ----below is brute force not optimal and also not passin all test cases---
//         // HashSet < Integer > set = new HashSet < > ();
//         // for (int i = 0; i < arr.length; i++) {
//         //     set.add(arr[i]);
//         // }
//         // int k = set.size();
//         // System.out.println(k);
//         // int j = 0;
//         // for (int x: set) {
//         //     arr[j] = x;
//         //     j++;
//         // }
       
//         // return k;
        
//     }
// }