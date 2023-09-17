#1502. Can Make Arithmetic Progression From Sequence

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # N = len(arr)
        # arr = set(arr)
        # n  = len(arr)
        # if n==1:
        #     return True
        # elif n!=N:
        #     return False
        # min_ = min(arr)
        # max_ = max(arr)
        
        # d = (2*sum(arr) - 2*min_*n)/(n*(n-1))
        
        # for i in range(min_,max_+1,int(d)):
        #     if i not in arr:
        #         return False
        # return True


        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != arr[1] - arr[0]:
                return False
        return True


p1=Solution()
print(p1.canMakeArithmeticProgression([3,5,1]))
