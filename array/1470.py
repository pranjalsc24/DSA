# shuffle array
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]





class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        
        # ls=[]
        # for i in range(n):
        #     ls+=[nums[i]]
        #     ls+=[nums[i+n]]
        # return ls  

        ans = []
        for i in range(n):
            # push x_1 .. x_n
            ans.append(nums[i])
            # push y_1 .. y_n
            ans.append(nums[i + n])
        return ans  

        # alternatively, we can do it in one-liner
        # return [x for p in zip(nums[:n], nums[n:]) for x in p] 
