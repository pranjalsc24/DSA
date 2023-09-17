# ------------- written in java also----------



class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        i=0
        pos=0
        while(i<len(arr)-1):
            if arr[i]<arr[i+1]:
                pos+=1
            else:
                return pos
            i+=1 


#    -------------using binary search---------
       

        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
