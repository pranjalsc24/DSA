# Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. 

# Note: Return 1, if there is at least one triplet following the condition else return 0.


# Input: n = 5, arr[] = {0, -1, 2, -3, 1}
# Output: 1
# Explanation: 0, -1 and 1 forms a triplet
# with sum equal to 0.


class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = arr[i] + arr[j] + arr[k]
                if sum == 0:
                    return True
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return False


