# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


# public class Solution {
#     public int[] sortArrayByParity(int[] nums) {
#         int[] result = new int[nums.length];
#         int evenIndex = 0;
#         int oddIndex = nums.length - 1;
        
#         for (int num : nums) {
#             if (num % 2 == 0) {
#                 result[evenIndex] = num;
#                 evenIndex++;
#             } else {
#                 result[oddIndex] = num;
#                 oddIndex--;
#             }
#         }
        
#         return result;
#     }
# }



# // class Solution {
# //     public int[] sortArrayByParity(int[] nums) {
# //         int left = 0;

# //         for (int i = 0; i < nums.length; i++) {
# //             if (nums[i] % 2 == 0) {
# //                 int temp = nums[left];
# //                 nums[left] = nums[i];
# //                 nums[i] = temp;
# //                 left++;
# //             }
# //         }

# //         return nums;        
# //     }
# // }










# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         even=[]
#         odd=[]
#         for i in nums:
#             if i%2==0:
#                 even.append(i)
            
#             else:
#                 odd.append(i)
            

#         res=even+odd
#         return res    
        