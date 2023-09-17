


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l,total=0,0
        res=float("inf")

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res= min(i-l+1,res)
                total -= nums[l]
                l +=1

        return 0 if res==float("inf") else res        


        
        
        
        
        
        # i = 0
        # j = 0
        # sum = 0
        # ans = 1000000
        
        # while j < len(nums):
        #     sum += nums[j]
            
        #     while sum >= target:
        #         ans = min(ans, j - i + 1)
        #         sum -= nums[i]
        #         i += 1
            
        #     j += 1
        
        # return 0 if ans == 1000000 else ans