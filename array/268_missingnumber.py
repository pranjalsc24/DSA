# Missing Number
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        # if len(nums)==1 and nums[0]==1:
        #     return 0

        if 0 not in nums:
            return 0

       
        maxx=1
        for i in range(len(nums)):
            
            if nums[i]==maxx:
                maxx+=1
            
            elif nums[i]<0:
                continue


        return maxx