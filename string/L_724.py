# Find Pivot Index

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum1=0
        sum2=0
        sum1=sum(nums)
        for i in range(len(nums)):
            sum1=sum1-nums[i]
            if sum1==sum2:
                return i
            sum2=sum2+nums[i] 
        return -1       

        