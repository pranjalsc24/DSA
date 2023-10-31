# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         map = {}
        
#         for num in nums:
#             map[num] = map.get(num, 0) + 1
        
       
#         for key, value in map.items():
#             if value == 1:
#                 return key
        
#         return 0

 
 
 
#  class Solution {
#     public int singleNonDuplicate(int[] nums) {
#          int n = nums.length;
#         Map<Integer, Integer> map = new HashMap<>();
        
#         for (int i = 0; i < n; i++) {
#             map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
#         }
        
       
#         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
#             if (entry.getValue() == 1) {
#                 return entry.getKey();
#             }
#         }
        
#         return 0;

#     }
#     }       
 