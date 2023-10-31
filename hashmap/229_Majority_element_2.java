// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: [3]
// Example 2:

// Input: nums = [1]
// Output: [1]
// Example 3:

// Input: nums = [1,2]
// Output: [1,2]

// class Solution {
//     public List<Integer> majorityElement(int[] nums) {
     
//         int n = nums.length;
//         ArrayList<Integer> res=new ArrayList<Integer>();
//         Map<Integer, Integer> map = new HashMap<>();
        
//         for (int i = 0; i < n; i++) {
//             map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
//         }
        
//         n = n / 3;
//         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
//             if (entry.getValue() > n) {
//                 // return entry.getKey();
//                 res.add(entry.getKey());
//             }
//         }
        
//         return res;
//     }
// }       
