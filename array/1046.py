#  Last Stone Weight

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.


# class Solution(object):
#     def lastStoneWeight(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: int
#         """
#         hq = list(map(neg, stones))
#         heapify(hq)

#         while len(hq) > 1 and hq[0] != 0:
#             heappush(hq, heappop(hq) - heappop(hq))
        
#         return -heappop(hq)