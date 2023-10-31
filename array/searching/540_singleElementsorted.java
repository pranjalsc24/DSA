// Example 1:

// Input: nums = [1,1,2,3,3,4,4,8,8]
// Output: 2
// Example 2:

// Input: nums = [3,3,7,7,10,11,11]
// Output: 10
 

// // // https://www.youtube.com/watch?v=AZOmHuHadxQ&t=1225s&ab_channel=takeUforward

// // class Solution {
// //     public int singleNonDuplicate(int[] nums) {

// //         int n=nums.length;
// //         if (n==1) return nums[0];
// //         if (nums[0] != nums[1]) return nums[0];
// //         if (nums[n-1] != nums[n-2]) return nums[n-1];

// //         int low=1;
// //         int high=n-2;

// //         while(low<=high){
// //             int mid= low + (high-low)/2;
// //             if(nums[mid] != nums[mid-1] && nums[mid]!=nums[mid+1]) return nums[mid];
// //             // we are in left
// //             if((mid%2==1 && nums[mid]==nums[mid-1]) || (mid%2==0 && nums[mid]==nums[mid+1])) {
// //                 low=mid+1;   //eliminate left half
// //             }
// //             // we are in right
// //             else{
// //                 high=mid-1;
// //             }
// //         }
// //         return -1;
// //     }
// // }


// // using hashmap

// class Solution {
//     public int singleNonDuplicate(int[] nums) {
//          int n = nums.length;
//         Map<Integer, Integer> map = new HashMap<>();
        
//         for (int i = 0; i < n; i++) {
//             map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
//         }
        
       
//         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
//             if (entry.getValue() == 1) {
//                 return entry.getKey();
//             }
//         }
        
//         return 0;

//     }
//     }



//     // -----------python-------------
//     class Solution:
//     def singleNonDuplicate(self, nums: List[int]) -> int:
//         n = len(nums)
//         map = {}
        
//         for num in nums:
//             map[num] = map.get(num, 0) + 1
        
       
//         for key, value in map.items():
//             if value == 1:
//                 return key
        
//         return 0

        