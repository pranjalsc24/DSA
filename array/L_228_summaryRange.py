class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # ---------- in below solution time is eceeded but undesrstood the concept

        # i=0
        # result=[]

        # if len(nums)==0:
        #     return []

        # while i<len(nums):
        #     j=i+1
        #     while(j<len(nums)):
        #         if nums[j-1]+1==nums[j]:
        #             j +=1
        #         else:
        #             break

        #         if nums[j-i]==1:
        #             result.append(str(nums[i]))
        #         else:
        #             result.append(str(nums[i]) + '->' + str(nums[j-1]))
        #         i=j
        # return result   



        if not nums: return []
        start = end = 0
        res=[]
        nums.append(nums[-1])
        for i in range (len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                end+=1
            else:
                if start<end:
                    res.append(str(nums[start])+"->"+str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = end = i+1
        return res

                                 
