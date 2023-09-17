#  How Many Numbers Are Smaller Than the Current Number






class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # l1 = sorted(nums)
        # return [l1.index(i) for i in nums]
        
        
        # res=[]
        # for i in range(len(nums)):
        #     count=0

        #     for j in range(len(nums)):
        #         if i != j and nums[i] > nums[j]:
        #             count +=1
        #     res.append(count)
            
        # return res   

        res=[]
        for i in range(len(nums)):
            count=0

            for j in range(len(nums)):
                if i == j:
                    continue
                    
                elif nums[i] > nums[j]:
                    count +=1
            res.append(count)
            
        return res    

                    
 

                    
