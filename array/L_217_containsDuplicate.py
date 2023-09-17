class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # ----------TIME IS EXCEEDED IN BELOW SOLUTION------
        # count=0
        # for i in nums:
        #     count= nums.count(i)
        #     if count>=2:
        #         return True
        # return False

        # THIS SOLUTION IS CORRECT
        number=set(nums)
        if len(nums)!=len(number):
            return True
        else:
            return False


        #  --------------one more solution----------
    #   ****IN THIS SOLUTION ALSO TIME IS EXCEEDED
        found=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False           