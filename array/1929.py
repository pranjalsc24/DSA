# conactenate array




class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # return nums *2
        # return nums+nums

        # -------another sol-------

        ans = []
        n = len(nums)
        for i in range(2*n):
            ans.append(nums[i%n])
        return ans 