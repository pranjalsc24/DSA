# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         map = {}
        
#         for num in nums:
#             map[num] = map.get(num, 0) + 1
        
#         n = n // 2
#         for key, value in map.items():
#             if value > n:
#                 return key
        
#         return 0


# class Solution {
#     public int majorityElement(int[] nums) {
#         int n = nums.length;
#         Map<Integer, Integer> map = new HashMap<>();
        
#         for (int i = 0; i < n; i++) {
#             map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
#         }
        
#         n = n / 2;
#         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
#             if (entry.getValue() > n) {
#                 return entry.getKey();
#             }
#         }
        
#         return 0;
#     }
# }       