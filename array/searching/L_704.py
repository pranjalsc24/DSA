# binary search
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #  ------linerar search---
        # for i in range(len(nums)):  
        #     if (nums[i] == target):  
        #         return i  
        # return -1

        # ----------binary search----------

        low=0
        high=len(nums)-1

        
        while low<=high:
            
            mid= (low+high)/2

            if nums[mid]==target:
                return mid
            elif (target<nums[mid]):
                high=mid-1
            else:
                low=mid+1
        return -1            





           
       