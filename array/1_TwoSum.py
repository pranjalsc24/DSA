#  Two Sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
      
        ans = [] # to store the indices of the two numbers
        for i in range(len(nums)): # loop through each element in the array
            for j in range(i+1, len(nums)): # loop through the rest of the array to find the other number
                sum = nums[i] + nums[j] # calculate the sum of the two numbers
                if sum == target: # check if the sum equals the target value
                    ans.append(i) # store the indices of the two numbers
                    ans.append(j)
                    return ans # return the answer
        return ans # if no such numbers exist, return an empty vector
    

# import java.util.*;
# class Solution {
#     public int[] twoSum(int[] nums, int target) {

#         // ArrayList<Integer> list=new ArrayList<Integer>();
#         for(int i=0;i<nums.length;i++){
#             for(int j=i+1;j<nums.length;j++){
#                 int sum=nums[i]+nums[j];
#                 if(sum==target){
#                     // list.add(i);
#                     // list.add(j);
#                     // return list.stream().mapToInt(Integer::intValue).toArray(); // convert List<Integer> to int[]
#                     return new int[] {i,j};
#                 }

#             }

#         }
#         // return list.stream().mapToInt(Integer::intValue).toArray(); // if no such numbers exist, return an empty array
#         return new int[0];
       

        
#     }
# }


# --------------striver---------------
# // ---------------------------better------------------
# // hashmap
# import java.util.HashMap;
# import java.util.Map;

# public class Solution {
#     public int[] twoSum(int[] nums, int target) {
#         Map<Integer, Integer> map = new HashMap<>();
#         int n = nums.length;
        
#         for (int i = 0; i < n; i++) {
#             int num = nums[i];
#             int moreNeeded = target - num;
            
#             if (map.containsKey(moreNeeded)) {
#                 return new int[] { map.get(moreNeeded), i };
#             }
            
#             map.put(num, i);
#         }
#     return new int[] { -1, -1 };
#     }
# }
