# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum=0
#         maxi=nums[0]
#         for i in range(len(nums)):
#             sum+=nums[i]
#             if sum>maxi:
#                 maxi=sum
#             if sum<0:
#                 sum=0
#         return maxi    
        

# class Solution {
#     public int maxSubArray(int[] nums) {
#         int sum=0;
#         int maxi=nums[0];
#         for(int i=0;i<nums.length;i++){
#             sum+=nums[i];
#             if(sum>maxi) maxi=sum;
#             if(sum<0)  sum=0;
#         }
#         return maxi;
#     }
# }

